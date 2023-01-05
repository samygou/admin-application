import typing as t

from zope.interface import Interface
from etcd3 import watch


glb_watch_cache = {}


class IWatchClient(Interface):
    """watchx interface"""

    def watch_(self, key: str, prefix_key: bool = False, **kwargs) -> t.Tuple:
        """

        :param key: watchx key
        :param prefix_key: 是否是前缀
        :param kwargs:
        :return: events, iterator
        """

    def cancel(self, watch_id):
        """

        :param watch_id:
        :return:
        """

    def add_watch_callback(self, key: str, callback: t.Callable, prefix_key: bool = False, **kwargs) -> int:
        """

        :param key: watchx key
        :param callback: 回调函数
        :param prefix_key: 是否前缀watch
        :param kwargs:
        :return: watch_id
        """

    def watch_response(self, key: str, prefix_key: bool = False, **kwargs) -> t.Tuple:
        """

        :param key: watchx key
        :param prefix_key: 是否前缀watch
        :param kwargs:
        :return: WatchResponse, iterator
        """

    def register(self, key: str, callback: t.Callable):
        """
        注册watch key的回调函数, 使用内部字典记录
        :param key: watchx key
        :param callback: 回调函数
        :return:
        """

    def global_callback(self, resp: watch.WatchResponse):
        """
        设置的全局回调函数
        :param resp: watchx response
        :return:
        """


class Client:
    """watchx client"""
    def __init__(self, cli: IWatchClient):
        """"""
        self._cli = cli

    def watch_(self, key: str, prefix_key=False, **kwargs):
        """

        :param key:
        :param prefix_key:
        :param kwargs:
        :return:
        """
        return self._cli.watch_(key, prefix_key=prefix_key, **kwargs)

    def cancel(self, watch_id: int):
        self._cli.cancel(watch_id)

    def add_watch_callback(self, key: str, callback: t.Callable, prefix_key: bool = False, **kwargs):
        """

        :param key:
        :param callback:
        :param prefix_key:
        :param kwargs:
        :return:
        """
        return self._cli.add_watch_callback(key, callback, prefix_key, **kwargs)

    def watch_response(self, key: str, prefix_key: bool = False, **kwargs) -> t.Tuple:
        """

        :param key:
        :param prefix_key:
        :param kwargs:
        :return:
        """
        return self._cli.watch_response(key, prefix_key, **kwargs)

    def register(self, key: str, callback: t.Callable):
        """
        注册watch key的回调函数, 使用内部字典记录
        :param key: watchx key
        :param callback: 回调函数
        :return:
        """
        self._cli.register(key, callback)

    def global_callback(self, resp: watch.WatchResponse):
        """
        设置的全局回调函数
        :param resp: watchx response
        :return:
        """
        self._cli.global_callback(resp)


def new_client(cli: IWatchClient) -> Client:
    return Client(cli)


def test_watch_callback(key: str, val: str):
    if not key:
        return

    keys = key.split('@', 1)
    prefix_key = keys[0]

    if prefix_key not in glb_watch_cache:
        glb_watch_cache[prefix_key] = {key: val} if val else 1
    else:
        if val:
            glb_watch_cache[prefix_key][key] = val
        else:
            if key in glb_watch_cache[prefix_key]:
                del glb_watch_cache[prefix_key][key]

    if not glb_watch_cache[prefix_key]:
        del glb_watch_cache[prefix_key]

    print(glb_watch_cache)

