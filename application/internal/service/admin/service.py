from zope.interface.declarations import implementer

from . import account, auth, company
from ... import biz
from application.interface import IBackend


@implementer(IBackend)
class Service(auth.AuthService, account.AccountService, company.CompanyService):
    """service 实例"""
    def __init__(
            self,
            account_use_case: biz.AccountUseCase,
            company_use_case: biz.CompanyUseCase
    ):
        """"""
        super(Service, self).__init__(account_use_case)
        super(auth.AuthService, self).__init__(account_use_case)
        super(account.AccountService, self).__init__(company_use_case)


def new_service(account_use_case: biz.AccountUseCase, company_use_case: biz.CompanyUseCase) -> Service:
    return Service(account_use_case, company_use_case)
