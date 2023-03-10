from functools import wraps

from flask import views, request, current_app
from pydantic import BaseModel

from application.internal.service.response import ResponseHandler
from application.exception import ExceptionCode


class AuthSendSmsReq(BaseModel):
    phone: str
    type: str


class AuthLoginReq(BaseModel):
    phone: str
    sms_token: str
    code: str


def login_required(func):
    @wraps(func)
    def verify_token(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return ResponseHandler.process(
                ExceptionCode.UNAUTH_CODE,
                'auth_token_invalid',
                'auth failed, no token'
            )

        if not current_app.r.b.check_auth(token):
            return ResponseHandler.process(
                ExceptionCode.UNAUTH_CODE,
                'auth_token_invalid',
                'auth token failed'
            )

        return func(*args, **kwargs)

    return verify_token


class AuthSendSmsResource(views.MethodView):
    """auth send sms resource"""
    def post(self):
        req = AuthSendSmsReq(**request.form)

        if not req.phone:
            return ResponseHandler.process(
                ExceptionCode.INVALID_PARAMS_CODE,
                'invalid_parameter',
                'phone must not be null'
            )

        if not req.type:
            return ResponseHandler.process(
                ExceptionCode.INVALID_PARAMS_CODE,
                'invalid_parameter',
                'type must not null'
            )

        token = current_app.r.b.send_sms(req)

        return ResponseHandler.process(
            ExceptionCode.SUCCESS,
            'success',
            'success',
            sms_token=token
        )


class AuthLoginResource(views.MethodView):
    """auth login resource"""
    def post(self):
        req = AuthLoginReq(**request.form)

        if not req.phone:
            return ResponseHandler.process(
                ExceptionCode.INVALID_PARAMS_CODE,
                'invalid_parameter',
                'phone must not be null'
            )

        if not req.sms_token:
            return ResponseHandler.process(
                ExceptionCode.INVALID_PARAMS_CODE,
                'invalid_parameter',
                'sms_token must not be null'
            )

        if not req.code:
            return ResponseHandler.process(
                ExceptionCode.INVALID_PARAMS_CODE,
                'invalid_parameter',
                'code must not be null'
            )

        token = current_app.r.b.login(req)

        return ResponseHandler.process(
            ExceptionCode.SUCCESS,
            'success',
            'success',
            token=token
        )


class AuthLogoutResource(views.MethodView):
    """auth logout resource"""
    def post(self):
        pass
