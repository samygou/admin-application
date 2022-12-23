from zope.interface.declarations import implementer

from application.internal.biz import ICompanyRepo


@implementer(ICompanyRepo)
class CompanyRepo:
    """company repo level"""

    def __init__(self):
        """初始化"""


def new_company_repo() -> CompanyRepo:
    return CompanyRepo()
