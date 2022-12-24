import typing as t

from zope.interface import Interface

from application.internal.modules.utils import Singleton


class IRegistration(Interface):
    """registration interface"""
    def register(self, key: str, val: t.Any) -> bool:
        """registration interface"""

    def deregister(self, key: str):
        """deregister interface"""


class Client(Singleton):
    """注册中心"""
    def __init__(self, cli: IRegistration):
        """init"""
        self._cli = cli

    def register(self, key: str, val: t.Any) -> bool:
        return self._cli.register(key, val)

    def deregister(self, key: str):
        self._cli.deregister(key)


def new_client(cli: IRegistration) -> Client:
    return Client(cli)
