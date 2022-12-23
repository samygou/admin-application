from . import account, company


__all__ = [
    'new_account_repo',
    'new_company_repo',
]

new_account_repo = account.new_account_repo
new_company_repo = company.new_company_repo
