import typing as t

from flask_apscheduler import APScheduler as _BaseAPScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from application.internal.modules.utils import Singleton


class APScheduler(_BaseAPScheduler, Singleton):
    def run_job(self, id, jobstore=None):
        with self.app.app_context():
            super().run_job(id=id, jobstore=jobstore)


def new_apscheduler(scheduler=BackgroundScheduler(timezone="Asia/Shanghai")) -> APScheduler:
    return APScheduler(scheduler=scheduler)
