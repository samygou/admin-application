#!/usr/bin/python
# encoding: utf-8
"""
@Author: Samy
@File: __init__.py
@Time: 2022/12/9
@desc:
"""
import os
import logging
import logging.handlers
import pathlib
import time
import traceback
import uuid
import sys

from flask import Flask, request, g, jsonify
from flask.logging import default_handler
from flask_cors import CORS
from flask_migrate import Migrate
from werkzeug.wrappers import Response
from werkzeug.exceptions import InternalServerError
import grpc

import settings
from application.exception import APIException, ExceptionCode
from application.internal.service.response import ResponseHandler
from application.internal.data import orm
from application.internal.data import cache
from application.internal.modules import apscheduler
from application.internal.modules.utils import Singleton
from application.internal.modules import redisx
from application.internal.modules import logx
from application.internal.modules import etcdx
from application.internal.modules import registration
from application.internal.modules import lockx
from application.internal.modules.kit_pb_sms import pb_kit_sms_pb2_grpc


class JSONResponse(Response):
    default_mimetype = 'application/json'
    default_status = 200

    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, dict):
            response = jsonify(response)

        return super(JSONResponse, cls).force_type(response, environ)


class FlaskX(Flask):
    response_class = JSONResponse

    def make_response(self, rv):
        status_code = 0
        if isinstance(rv, dict):
            rv['cost_time'] = f'{int(time.time() * 1000) - g.start_time} ms'
            rv['request_id'] = str(uuid.uuid4())
            if 'code' not in rv:
                rv['code'] = 0
            if 'status_code' in rv:
                status_code = rv.pop('status_code')

        response = super(FlaskX, self).make_response(rv)
        if status_code:
            response.status_code = status_code

        return response


def _configure_logger(app: FlaskX):
    app.logger.removeHandler(default_handler)

    logx.Logger(
        pathlib.Path(os.path.join(settings.BASE_DIR, 'logs')).as_posix(),
        'admin_application.log'
    ).init()


def _configure_handlers(app: FlaskX):
    @app.before_request
    def before_request():
        g.start_time = int(time.time() * 1000)

    @app.after_request
    def after_request(response):
        logging.info(f'request path: {request.path}, cost time: {int(time.time() * 1000) - g.start_time} ms')

        return response


def _register_exception(app: FlaskX):
    """注册异常处理"""
    @app.errorhandler(Exception)
    def handle_exception(exc):
        """添加需要特殊处理的异常, 不用做处理的异常, 直接返回"""
        if isinstance(exc, APIException):
            return exc.to_dict()

        if isinstance(exc, InternalServerError):
            exc_type, exc_value, exc_traceback = sys.exc_info()
            err_info = traceback.format_exception(exc_type, exc_value, exc_traceback)
            err_type = err_info[-1].split(":")[0]

            logging.info(f'err_type: {err_type}')
            logging.exception(exc)

            return ResponseHandler.process(ExceptionCode.INTERNAL_ERR_CODE, 'server_err', '服务器异常')

        return exc


def _register_blueprint(app: FlaskX):
    from .api.v1.admin import api_router

    app.register_blueprint(api_router)


def _register_server(app: FlaskX):
    from application.internal.server import new_http_server
    from application.internal.service.admin import new_service
    from application.internal.biz import new_account_use_case, new_company_use_case
    from application.internal.data import new_account_repo, new_company_repo

    # -----------repo------------
    account_use_case = new_account_use_case(new_account_repo())
    company_use_case = new_company_use_case(new_company_repo())

    # -----------biz------------
    service = new_service(account_use_case, company_use_case)

    # -----------service-----------
    router = new_http_server(service)

    # 注册到app中, 利用python动态添加属性的功能
    app.r = router


def run_grpc_server(port: int):
    from application.internal.server import new_grpc_server
    from application.internal.service.service import new_app_service
    from application.internal.biz import new_account_use_case, new_company_use_case
    from application.internal.data import new_account_repo, new_company_repo

    from flask import current_app

    # -----------repo------------
    account_use_case = new_account_use_case(new_account_repo())
    company_use_case = new_company_use_case(new_company_repo())

    # -----------biz------------
    grpc_service = new_app_service(account_use_case, company_use_case)

    rpc = new_grpc_server(port, grpc_service, options=[('grpc.max_receive_message_length', 30 * 1024 * 1024)])

    logging.info('run grpc server success')

    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        rpc.server.stop(0)


def _register_db(app: FlaskX):
    # orm
    orm.db.init_app(app)

    # migrate
    Migrate(app, orm.db)


def _register_cors(app: FlaskX):
    cors = CORS()
    cors.init_app(app)


def _register_redis(app: FlaskX):
    conf = app.config['REDISCONF']()
    redisx.redis = redisx.new_client(**conf.dict())
    redisx.redis.cli.init_app(app)


def _register_cache(app: FlaskX):
    cache.sess = cache.new_cache_session(redisx.redis)


def _register_apscheduler(app: FlaskX):
    apscheduler.cli = apscheduler.new_apscheduler()
    apscheduler.cli.init_app(app)

    if not apscheduler.cli.running:
        apscheduler.cli.start()


def _register_etcd(app: FlaskX):
    """"""
    etcdx.cli = etcdx.new_client(
        grpc_options=
        {
            'grpc.http2.true_binary': 1,
            'grpc.http2.max_pings_without_data': 0,
        }.items()
    )
    etcdx.cli.conn(etcdx.EtcdConnType.GRPC)


def _register_registration_center(app: FlaskX):
    registration.cli = registration.new_client(etcdx.cli.registration())

    # 测试etcd的注册功能
    # registration.cli.register('admin-application-registration-test2', 'http://127.0.0.1:30003')


def _register_distributed_lock(app: FlaskX, pool: int = 10):
    lockx.lock_pool = lockx.LockPool(pool)
    for _ in range(pool):
        lockx.lock_pool.put(lockx.Lock(redisx.Lock(client=redisx.redis)))
        # lockx.lock_pool.put(lockx.Lock(etcdx.Lock(client=etcdx.cli)))


def _register_grpc(app: FlaskX):
    options = [('grpc.max_receive_message_length', 10 * 1024 * 1024)]
    channel = grpc.insecure_channel(app.config['GRPC_HOST_SMS'], options=options)
    app.sms_api = pb_kit_sms_pb2_grpc.APIStub(channel)


def _register_new_modules(app: FlaskX):
    _register_server(app)
    _register_db(app)
    _register_redis(app)
    _register_cache(app)
    _register_cors(app)
    _register_apscheduler(app)
    _register_etcd(app)
    _register_registration_center(app)
    _register_distributed_lock(app)
    _register_grpc(app)


class CreateAppX:
    """create app"""

    def __init__(self):
        pass

    @staticmethod
    def create_app(config_name: str = 'default'):
        app = FlaskX(__name__)
        app.config.from_object(settings.config[config_name])
        settings.config[config_name].init_app(app)

        _configure_logger(app)
        _configure_handlers(app)
        _register_exception(app)
        _register_blueprint(app)
        _register_new_modules(app)

        return app
