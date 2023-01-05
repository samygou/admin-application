import typing as t

from . import watch


__all__ = [
    'IWatchClient',
    'Client',
    'new_client',
    'test_watch_callback'
]


IWatchClient = watch.IWatchClient
Client = watch.Client
new_client = watch.new_client
cli: t.Optional[Client] = None
test_watch_callback = watch.test_watch_callback
