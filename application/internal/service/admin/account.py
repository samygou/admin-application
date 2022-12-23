import typing as t

from application.internal import biz
from application.api.v1 import admin


class AccountService:
    """account service"""
    def __init__(self, account_use_case: biz.AccountUseCase):
        self._account_use_case = account_use_case

    def list_accounts(self, req: admin.ListAccountReq) -> t.List[admin.ListAccountResp]:
        accounts = self._account_use_case.list_accounts(
            biz.ListAccountReq(**req.dict())
        )
        accounts = list(map(lambda account: admin.ListAccountResp(**account.dict()), accounts))

        return accounts
