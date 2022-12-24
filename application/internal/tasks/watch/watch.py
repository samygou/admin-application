from threading import Thread

from etcd3 import events

from application.internal.modules.utils import Singleton
from application.internal.modules import etcdx


class Watch(Singleton):
    """watch task"""
    def __init__(self, cli: etcdx.Client):
        """"""
        self._cli = cli

    def add_watch(self, key: str, prefix_key=False, **kwargs):
        """

        :param key:
        :param prefix_key:
        :param kwargs:
        :return:
        """
        self._cli.watch(key, prefix_key=prefix_key, **kwargs)

    def _register_watch(self):
        """注册新的watch"""

    def run(self):
        pass

