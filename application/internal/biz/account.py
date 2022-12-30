import re
import time
import typing as t
import logging

import jwt
from pydantic import BaseModel, Field
from zope.interface import Interface
from flask import current_app, g

from application.exception import APIException, ExceptionCode
from application.internal.modules import pagex
from application.internal.modules.kit_pb_sms import pb_kit_sms_pb2
from application.internal.modules.jwt import format_, parse


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

    def exist_account_by_uid(self, uid: str) -> bool:
        """
        通过uid判断账户是否存在
        :param uid:
        :return:
        """

    def get_account_by_uid(self, uid: str) -> t.Optional[Account]:
        """

        :param uid:
        :return:
        """

    def get_account_by_phone(self, phone: str) -> t.Optional[Account]:
        """

        :param phone:
        :return:
        """

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

        try:
            resp = current_app.sms_api.SendSM(pb_kit_sms_pb2.SendSMReq(
                phone=req.phone,
                typ=req.type,
                expired=5 * 60
            ))
        except Exception as e:
            logging.error(e)
            raise APIException(
                ExceptionCode.INTERNAL_ERR_CODE,
                'server_err',
                'internal default'
            )

        if resp.err != pb_kit_sms_pb2.OK:
            logging.warning(f'短信平台发送失败: {resp}')
            raise APIException(
                ExceptionCode.INTERNAL_ERR_CODE,
                'server_err',
                'internal default'
            )

        return resp.token

    def login(self, req: AuthLoginReq) -> str:
        if not re.match(r'^1[3456789][0-9]{9}$', req.phone):
            raise APIException(
                ExceptionCode.INVALID_PARAMS_CODE,
                'invalid_parameter',
                'cell phone number is not exactly'
            )

        account = self._repo.get_account_by_phone(req.phone)
        if not account:
            raise APIException(
                ExceptionCode.NOT_FOUND_CODE,
                'account_not_exist',
                'account is not exist'
            )

        try:
            resp = current_app.sms_api.CheckCode(pb_kit_sms_pb2.CheckCodeReq(
                phone=req.phone,
                token=req.sms_token,
                code=req.code
            ))
        except Exception as e:
            logging.error(e)
            raise APIException(
                ExceptionCode.INTERNAL_ERR_CODE,
                'server_err',
                'internal default'
            )

        if resp.err != pb_kit_sms_pb2.OK:
            if resp.err == pb_kit_sms_pb2.TokenExpired:
                logging.info('token expired')
                raise APIException(
                    ExceptionCode.UNAUTH_CODE,
                    'auth_failed',
                    'token expired'
                )
            elif resp.err == pb_kit_sms_pb2.InvalidCode:
                logging.info('invalid code')
                raise APIException(
                    ExceptionCode.UNAUTH_CODE,
                    'auth_failed',
                    'invalid code'
                )
            elif resp.err == pb_kit_sms_pb2.InvalidToken:
                logging.info('invalid token')
                raise APIException(
                    ExceptionCode.UNAUTH_CODE,
                    'auth_failed',
                    'invalid token'
                )
            else:
                logging.warning(f'check code failed: {resp}')
                raise APIException(
                    ExceptionCode.INTERNAL_ERR_CODE,
                    'server_err',
                    'internal err'
                )

        payload = {'uid': account.uid, 'expired': int(time.time()) + current_app.config['TOKEN_EXPIRED']}
        token = format_(payload, current_app.config['JWT_SECRET'])

        return token

    def check_auth(self, token: str) -> bool:
        """
        biz check auth
        :param token:
        :return:
        """
        try:
            payload = parse(token, current_app.config['JWT_SECRET'])
        except Exception as e:
            logging.error(e)
            raise APIException(
                ExceptionCode.UNAUTH_CODE,
                'auth_token_invalid',
                'auth token invalid'
            )

        if 'uid' not in payload or 'expired' not in payload:
            logging.info('uid or expired not in payload')
            raise APIException(
                ExceptionCode.UNAUTH_CODE,
                'auth_token_failed',
                'token incomplete'
            )

        account = self._repo.get_account_by_uid(payload['uid'])
        if not account:
            logging.info('account not exist, auth failed')
            raise APIException(
                ExceptionCode.UNAUTH_CODE,
                'auth_token_failed',
                'account not exist, auth failed'
            )

        if payload['expired'] < int(time.time()):
            logging.info('授权过期')
            raise APIException(
                ExceptionCode.UNAUTH_CODE,
                'auth_token_expired'
                'token expired'
            )

        g.account = account

        return True

    def list_accounts(self, req: ListAccountReq) -> t.List[Account]:
        """

        :param req:
        :return:
        """
        accounts = self._repo.list_accounts(req)

        return accounts


def new_account_use_case(repo: IAccountRepo) -> AccountUseCase:
    return AccountUseCase(repo)
