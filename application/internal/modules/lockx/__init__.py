from . import lock


__all__ = [
    'Lock',
    'LockCli',

    'new_lock_cli_map'
]


Lock = lock.Lock
LockCli = lock.LockCli

new_lock_cli_map = lock.new_lock_cli_map
