import logging

from flask import current_app

from application.internal.biz import AccountUseCase, CompanyUseCase
from application.api.v1.app import admin_pb2
from application.api.v1.app import admin_pb2_grpc


class AdminService(admin_pb2_grpc.AdminServicer):
    """service 实例, grpc服务"""
    def __init__(
            self,
            accountUseCase: AccountUseCase,
            companyUseCase: CompanyUseCase
    ):
        self._accountUseCase = accountUseCase
        self._companyUseCase = companyUseCase

    def GetAccountByPhone(self, request, context):
        logging.info(request.phone)

        account, err = self._accountUseCase.get_account_by_phone(request.phone)

        return admin_pb2.GetAccountByUIDReply(account=admin_pb2.Account(
            uid=account.uid,
            name=account.name,
            phone=account.phone,
            remark=account.remark
        ), err=err)

    def GetAccountByUID(self, request, context):

        account, err = self._accountUseCase.get_account_by_uid(request.uid)

        return admin_pb2.GetAccountByUIDReply(account=admin_pb2.Account(
            uid=account.uid,
            name=account.name,
            phone=account.phone,
            remark=account.remark
        ), err=err)

    def ListCompanies(self, request, context):

        out, err = self._companyUseCase.list_companies()

        return admin_pb2.ListCompaniesReply(companies=out, err=err)

    def ListCompaniesByUIDs(self, request, context):

        out, err = self._companyUseCase.list_companies_by_uids(request.uid)

        return admin_pb2.ListCompaniesReply(companies=out, err=err)


def new_service(
        account_use_case: AccountUseCase,
        company_use_case: CompanyUseCase,
) -> AdminService:
    return AdminService(account_use_case, company_use_case)
