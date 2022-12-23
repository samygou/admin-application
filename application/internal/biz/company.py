import typing as t

from zope.interface import Interface
from pydantic import BaseModel


class Company(BaseModel):
    uid: str
    name: str
    modules: t.List
    expired: int
    config: t.List


class ICompanyRepo(Interface):
    """company repo interface"""


class CompanyUseCase:
    """company use case"""

    def __init__(
            self,
            repo: ICompanyRepo,
    ):
        self._repo = repo

    def list_companies(self) -> t.List[Company]:
        """获取公司列表"""
        return []

    def list_companies_by_uids(self, uids: t.List[str]) -> t.List[Company]:
        """根据 uids 获取公司列表"""
        return []


def new_company_use_case(repo: ICompanyRepo) -> CompanyUseCase:
    return CompanyUseCase(repo)
