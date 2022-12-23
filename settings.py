#!/usr/bin/python
# encoding: utf-8
"""
@Author: Samy
@File: settings.py
@Time: 2022/12/8
@desc: 
"""
import os

from pydantic import BaseModel

BASE_DIR = os.path.realpath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '2ce67783b5204a546a5946e3bbf695c0'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_POOL_RECYCLE = 299  # 设置为小于5分钟
    SQLALCHEMY_POOL_TIMEOUT = 20

    # 配置缓存
    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = '127.0.0.1'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 1
    CACHE_REDIS_PASSWORD = ''

    _SERVER_NAME = 'admin-application'

    # 分页配置项
    PAGE_SIZE = 10

    # interval time
    INTERVAL_TIME = 20 * 60
    INTERVAL_MINUTE = 20

    JWT_SECRET = 'qk9@tP-p*379BU2mZsmgkUf_Ub9Nv9C-@*ZgNvZmg6P-HJhVr*9kXRPZJX8b9j@Z'

    REDIS_URL = 'redis://localhost:6379'

    # 配置redis的分布式锁
    REDIS_LOCK_EXPIRED = 30
    REDIS_LOCK_TIMEOUT = 40

    # 缓存默认时间
    CACHE_DEFAULT_TIME = 1800

    class REDISCONF(BaseModel):
        max_connections: int = 20
        decode_responses: bool = False
        db: int = 3

    # rpc
    class RPC:
        APP_HOST = '127.0.0.1:30003'
        OPTIONS = {'max_recv': 10 * 1024 * 1024}  # 配置options信息, 这里配置默认最大接收数据为10M

    @staticmethod
    def init_app(app):
        pass


class LocalConfig(Config):
    DEBUG = False

    # mysql配置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') \
                              or 'mysql+pymysql://root:123456@127.0.0.1/admin_application_db?charset=utf8mb4'

    SQLALCHEMY_BINDS = {

    }


class DevelopmentConfig(Config):
    DEBUG = False

    # mysql配置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') \
                              or 'mysql+pymysql://root:123456@127.0.0.1/admin_application_db?charset=utf8mb4'

    SQLALCHEMY_BINDS = {

    }


class ProductionConfig(Config):
    DEBUG = False

    # mysql数据库配置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') \
                              or 'mysql+pymysql://root:123456@127.0.0.1/admin_application_db?charset=UTF8MB4'

    SQLALCHEMY_BINDS = {

    }


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'local': LocalConfig,
    'default': LocalConfig,
}
