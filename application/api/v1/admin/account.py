import typing as t

from flask import views, request, current_app
from pydantic import BaseModel, Field

from application.internal.service.response import ResponseHandler
from application.exception import ExceptionCode
from application.internal.modules import pagex


class ListAccountReq(BaseModel):
    uid: t.Optional[str] = None
    phone: t.Optional[str] = None
    username: t.Optional[str] = None
    page_limit: t.Optional[pagex.Pagex] = pagex.Pagex()


class ListAccountResp(BaseModel):
    uid: str
    username: str
    phone: str
    remark: str


class AccountResource(views.MethodView):
    """account resource"""
    def get(self):
        pl = request.args.get('pl').split(',', 1)
        page_limit = pagex.Pagex(offset=int(pl[0]), size=int(pl[1]))
        req = ListAccountReq(**request.args)
        req.page_limit = page_limit

        accounts = current_app.r.b.list_accounts(req)
        accounts = list(map(lambda account: account.dict(), accounts))

        return ResponseHandler.process(
            ExceptionCode.SUCCESS,
            'success',
            'success',
            accounts=accounts,
        )
