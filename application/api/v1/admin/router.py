from flask import Blueprint

from .auth import AuthSendSmsResource, AuthLoginResource, AuthLogoutResource
from .company import CompanyResource
from .account import AccountResource


# new blue print
api_router = Blueprint('root', __name__, url_prefix='/api')
account = Blueprint('account', __name__, url_prefix='/account')
auth = Blueprint('auth', __name__, url_prefix='/auth')
company = Blueprint('company', __name__, url_prefix='/company')

# auth模块
api_router.register_blueprint(auth)
auth.add_url_rule(rule='/send_sms', endpoint='auth_send_sms', view_func=AuthSendSmsResource.as_view('send_sms'))
auth.add_url_rule(rule='/login', endpoint='auth_login', view_func=AuthLoginResource.as_view('login'))
auth.add_url_rule(rule='/logout', endpoint='auth_logout', view_func=AuthLogoutResource.as_view('logout'))

# account 模块
api_router.register_blueprint(account)
account.add_url_rule(rule='/accounts', endpoint='accounts', view_func=AccountResource.as_view('accounts'))
account.add_url_rule(rule='/accounts/<id>', endpoint='accounts_id')

# company 模块
api_router.register_blueprint(company)
company.add_url_rule(rule='/companies', endpoint='company_companies', view_func=CompanyResource.as_view('companies'))
