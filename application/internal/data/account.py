import logging
import time
import typing as t

from zope.interface.declarations import implementer
from flask import current_app

from .. import biz
from .tables import Account
from . import orm
from . import cache


@implementer(biz.IAccountRepo)
class AccountRepo:
    """account data level"""

    def __init__(self):
        pass

    def exist_account_by_phone(self, phone: str) -> bool:
        account = Account.query.filter(Account.phone == phone).first()
        if not account:
            return False

        with orm.DBSession(orm.db) as sess:
            pass

        return True

    def list_accounts(self, req: biz.ListAccountReq) -> t.List[biz.Account]:
        """

        :param req:
        :return:
        """
        with cache.sess.context() as sess:
            cache_name = f"""{current_app.config['_SERVER_NAME']}-list-accounts"""
            if req.uid:
                cache_name = f'{cache_name}-{req.uid}'
            if req.phone:
                cache_name = f'{cache_name}-{req.phone}'
            if req.username:
                cache_name = f'{cache_name}-{req.username}'
            opts = cache.CacheOptions(
                cacheType=cache.CacheType.LIST,
                rangeIdx=cache.RangeIdx(
                    start=req.pl.offset,
                    end=req.pl.offset+req.pl.size
                )
            )
            cache_expired = current_app.config.get('CACHE_DEFAULT_TIME', 1800)
            accounts = sess.cache(
                cache_name,
                opts,
                cache_expired,
                cacheWaitTimeout=30,
                lockExpired=5,
                req=req,
                get_cache_from_db_func=self.list_accounts_from_db
            )

        accounts = accounts if accounts else []
        accounts = list(map(lambda account: biz.Account(**account), accounts))

        return accounts

    @staticmethod
    def list_accounts_from_db(req: biz.ListAccountReq) -> t.List[t.Dict]:
        """"""
        query = Account.query
        if req.uid:
            query = query.filter(Account.uid == req.uid)
        if req.phone:
            query = query.filter(Account.phone == req.phone)
        if req.username:
            query = query.filter(Account.username == req.username)
        if req.pl:
            query = query.offset(req.pl.offset).limit(req.pl.size)
        accounts = query.all()
        accounts = list(map(lambda account: biz.Account.from_orm(account).dict(), accounts))

        return accounts


def new_account_repo() -> AccountRepo:
    return AccountRepo()
