import logging
import traceback
from functools import wraps
import typing as t

try:
    from synchronize import make_synchronized
except ImportError:
    import threading

    def make_synchronized(func):
        """
        用于实现单例并保证线程安全的装饰器
        """
        func.__lock__ = threading.Lock()

        def synced_func(*args, **kws):
            with func.__lock__:
                return func(*args, **kws)

        return synced_func


class Singleton(object):
    @make_synchronized
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = object.__new__(cls)
        return cls._instance


class NoException:
    """不抛出异常"""
    def __init__(self):
        """"""

    def __call__(self, func):
        @wraps(func)
        def wrappers(*args, **kwargs) -> t.Callable:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.error(e)
                traceback.print_exc()

            logging.info(f'func {func.__name__} do not raise Exception')

        return wrappers
