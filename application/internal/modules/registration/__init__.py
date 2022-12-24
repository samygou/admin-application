import typing as t

from . import registration


__all__ = ['cli', 'new_client', 'IRegistration']

Client = registration.Client
cli: t.Optional[Client] = None
new_client = registration.new_client

IRegistration = registration.IRegistration
