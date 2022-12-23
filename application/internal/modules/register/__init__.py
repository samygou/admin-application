import typing as t

from . import register


__all__ = ['Client', 'cli', 'new_client']

Client = register.Client
cli: t.Optional[Client] = None
new_client = register.new_client
