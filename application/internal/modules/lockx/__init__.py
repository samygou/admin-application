import typing as t

from . import lock


__all__ = [
    'Lock',
    'ILock',
    'LockPool',
]


Lock = lock.Lock
ILock = lock.ILock
LockPool = lock.LockPool

lock_pool: t.Optional[LockPool] = None
