import typing as t

from application.internal import biz

from application.api.v1.admin import (
    ListCompaniesReq,
    ListCompaniesResp
)


class CompanyService:
    """company service"""
    def __init__(self, company_use_case: biz.CompanyUseCase):
        self._company_use_case = company_use_case

    def list_companies(self, req: ListCompaniesReq) -> t.List[ListCompaniesResp]:
        # print(req)
        #
        # companies = []
        # companies.append(ListCompaniesResp(
        #     uid='12345',
        #     name='samy',
        #     modules=[],
        #     expired=0,
        #     config={}
        # ))
        companies = self._company_use_case.list_companies()

        return companies
