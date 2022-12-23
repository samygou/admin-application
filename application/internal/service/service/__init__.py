from . import service


__all__ = [
    'new_app_service',
    'AdminService'
]

new_app_service = service.new_service
AdminService = service.AdminService
