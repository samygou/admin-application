from application.api.v1 import admin
from application.internal import biz


class AuthService:
    """auth service handler"""
    def __init__(self, account_use_case: biz.AccountUseCase):
        self._account_use_case = account_use_case

    def send_sms(self, req: admin.AuthSendSmsReq) -> str:
        token = self._account_use_case.send_sms(biz.AuthSendSmsReq(phone=req.phone, type=req.type))

        return token

    def login(self, req: admin.AuthLoginReq) -> str:
        token = self._account_use_case.login(biz.AuthLoginReq(
            phone=req.phone,
            sms_token=req.sms_token,
            code=req.code
        ))

        return token
