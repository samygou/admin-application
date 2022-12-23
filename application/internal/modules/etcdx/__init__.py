import typing as t

from . import etcdx


__all__ = [
    'Client',
    'new_client',
    'cli',
    'EtcdConnType',
]

Client = etcdx.Client
new_client = etcdx.new_client
cli: t.Optional[Client] = None
EtcdConnType = etcdx.EtcdConnType
