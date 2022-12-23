import typing as t

from . import redisx


__all__ = ['new_client', 'Client', 'redis']

new_client = redisx.new_client
Client = redisx.Client
redis: t.Optional[Client] = None
