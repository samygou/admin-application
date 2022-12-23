import typing as t

from flask import views, request, current_app
from pydantic import BaseModel

from application.internal.service.response import ResponseHandler
from application.exception import ExceptionCode


class ListCompaniesReq(BaseModel):
    """list companies req"""
    offset: int
    size: int


class ListCompaniesResp(BaseModel):
    uid: str
    name: str
    modules: t.List
    expired: int
    config: t.Dict


class CompanyResource(views.MethodView):
    """company resource"""
    def get(self):
        req = ListCompaniesReq(**request.args)

        companies = current_app.r.b.list_companies(req)
        companies = list(map(lambda company: company.dict(), companies))

        return ResponseHandler.process(
            ExceptionCode.SUCCESS,
            'success',
            'success',
            companies=companies,
        )
