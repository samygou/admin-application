import re
import typing as t

from pydantic import BaseModel, Field
from zope.interface import Interface

from application.exception import APIException, ExceptionCode
from application.internal.modules import pagex
from application.api.v1.app import admin_pb2


class AuthSendSmsReq(BaseModel):
    phone: str
    type: str


class AuthLoginReq(BaseModel):
    phone: str
    sms_token: str
    code: str


class Account(BaseModel):
    uid: str
    username: str
    phone: str
    remark: str

    class Config:
        orm_mode = True


class ListAccountReq(BaseModel):
    uid: t.Optional[str] = None
    phone: t.Optional[str] = None
    username: t.Optional[str] = None
    pl: t.Optional[pagex.Pagex] = Field(alias='page_limit')


class IAccountRepo(Interface):
    """account data level interface"""

    def exist_account_by_phone(self, phone: str) -> bool:
        """
        判断账户是否存在
        :param phone: phone number
        :return: bool, is exist or not
        """""

    def list_accounts(self, req: ListAccountReq) -> t.List[Account]:
        """list accounts"""


class AccountUseCase:
    """account biz use case"""
    def __init__(self, repo: IAccountRepo):
        self._repo = repo

    def send_sms(self, req: AuthSendSmsReq) -> str:
        if not re.match(r'^1[3456789][0-9]{9}$', req.phone):
            raise APIException(
                ExceptionCode.INVALID_PARAMS_CODE,
                'invalid_parameter',
                'cell phone number is not exactly'
            )

        if req.type not in ['login', 'registration']:
            raise APIException(
                ExceptionCode.INVALID_PARAMS_CODE,
                'invalid_parameter',
                'type is not exactly'
            )

        if not self._repo.exist_account_by_phone(req.phone):
            raise APIException(
                ExceptionCode.NOT_FOUND_CODE,
                'account_not_exist',
                'account is not exist'
            )

        return "sms_token_ah363632"

    def login(self, req: AuthLoginReq) -> str:
        return "login_token_3473473473434"

    def get_account_by_phone(self, phone: str) -> (Account, admin_pb2.Error):
        return Account(uid='123456', name='samy', phone='13005496008', remark=''), admin_pb2.OK

    def get_account_by_uid(self, uid: str) -> (Account, admin_pb2.Error):
        return Account(uid='123456', name='samy', phone='13005496008', remark=''), admin_pb2.OK

    def list_accounts(self, req: ListAccountReq) -> t.List[Account]:
        """

        :param req:
        :return:
        """
        accounts = self._repo.list_accounts(req)

        return accounts


def new_account_use_case(repo: IAccountRepo) -> AccountUseCase:
    return AccountUseCase(repo)
