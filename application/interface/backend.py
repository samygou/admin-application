import typing as t

from zope.interface import Interface

from application.api.v1.admin import (
    AuthSendSmsReq,
    AuthLoginReq,

    ListAccountReq,
    ListAccountResp,

    ListCompaniesReq,
    ListCompaniesResp,
)


class IBackend(Interface):
    """api层接口"""

    def send_sms(self, req: AuthSendSmsReq) -> str:
        """
        发送短信
        :param req: send sms request args
        :return: sms_token
        """

    def login(self, req: AuthLoginReq) -> str:
        """

        :param req: login request args
        :return: token, login token
        """

    def list_accounts(self, req: ListAccountReq) -> t.List[ListAccountResp]:
        """

        :return:
        """

    def list_companies(self, req: ListCompaniesReq) -> t.List[ListCompaniesResp]:
        """

        :param req:
        :return:
        """


class RouterHandle:
    """路由操作句柄"""
    def __init__(self, backend: IBackend):
        self.b = backend


def new_router_handler(backend: IBackend) -> RouterHandle:
    return RouterHandle(backend)
