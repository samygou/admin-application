import typing as t

from . import scheduler


__all__ = ['APScheduler', 'new_apscheduler', 'cli']

APScheduler = scheduler.APScheduler
new_apscheduler = scheduler.new_apscheduler
cli: t.Optional[APScheduler] = None
