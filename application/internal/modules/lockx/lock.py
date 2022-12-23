from enum import Enum, unique
import typing as t
import logging
import traceback

from application.internal.modules import redisx
from application.internal.modules.utils import Singleton, NoException


@unique
class LockCli(Enum):
    REDIS = 0
    ETCD = 1


lock_cli_map: t.Optional[t.Dict[LockCli, t.Any]] = {}


def new_lock_cli_map(_lock_cli_map):
    return _lock_cli_map


class Lock(Singleton):
    """"""
    def __init__(
            self,
            name: str,
            ttl: int = 60,
            lockType: LockCli = LockCli.REDIS
    ):
        """
        初始化分布式锁, 目前可选择redis和etcd
        注: with 上下文模式慎用, 如果是大量线程同时获取锁的时候, 会不断的加锁 -> 释放锁, 因为退出with的时候会自动释放锁
        :param name: lock name
        :param ttl: lock expired, seconds
        :param lockType: 分布式锁的类型
        """
        self._cli = redisx.redis if not lock_cli_map.get(lockType) else lock_cli_map.get(lockType)
        self._name = name
        self._ttl = ttl
        self._lock = self._cli.lock(name, ttl)

    @property
    def name(self):
        return self._name

    @property
    def ttl(self):
        return self._ttl

    @NoException()
    def acquire(self) -> bool:
        """
        acquire lock, etcd retry raise Exception, catch it and do not raise
        :return:
        """
        return self._lock.acquire()

    @NoException()
    def release(self):
        """
        release lock
        :return:
        """
        self._lock.release()

    @NoException()
    def is_acquired(self) -> bool:
        """判断是否是自己家的锁"""
        return self._lock.is_acquired()

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()
