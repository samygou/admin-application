import typing as t
import logging

from pydantic import BaseModel

from application.internal.modules import etcdx
from application.internal.modules import apscheduler


class TTLOptions(BaseModel):
    heartBeat: int
    ttl: int


class Client:
    """"""
    def __init__(self, cli: etcdx.Client, ttlOptions: t.Optional[TTLOptions] = None):
        """"""
        self._cli = cli
        self._ttl_options = ttlOptions if ttlOptions else TTLOptions(heartBeat=5, ttl=10)
        self.lease_info: t.Optional[t.Dict] = {}

    def register(self, key: str, value: t.Any) -> bool:
        """

        :param key:
        :param value:
        :return:
        """
        if not key or not value:
            return False

        lease = self._cli.lease(self._ttl_options.ttl)
        lease_id = lease.id

        prev_kv = self._cli.put(key, value, lease=lease)
        logging.info(f'prev_kv: {prev_kv}')

        self.lease_info[key] = lease

        self._cli.lease_keepalive(lease_id, self._ttl_options.heartBeat)

        # apscheduler.cli.add_job(
        #     id='test-delete-lease-job',
        #     func=self.deregister,
        #     args=(key,),
        #     trigger='interval',
        #     seconds=60
        # )

        logging.info('register ok')

        return True

    def deregister(self, key: str):
        if not key:
            return

        self._cli.delete(key)

        lease = self.lease_info.get(key, None)

        if lease:
            # 1. 停止lease
            self._cli.revoke_lease(lease.id)

            # 3. 删除 key
            del self.lease_info[key]

    def watch(self, key: str, prefix_key=False, **kwargs):
        """

        :param key:
        :param prefix_key:
        :param kwargs:
        :return:
        """


def new_client(cli: etcdx.Client) -> Client:
    return Client(cli)
