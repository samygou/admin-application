import logging
import typing as t
from enum import Enum, unique

import etcd3

from application.internal.modules.utils import Singleton
from application.internal.modules import apscheduler


@unique
class EtcdConnType(Enum):
    HTTP = 0
    GRPC = 1


class Client(Singleton):
    """etcd client"""
    def __init__(
            self,
            host: str = 'localhost',
            port: int = 2379,
            ca_cert=None,
            cert_key=None,
            cert_cert=None,
            timeout=None,
            user=None,
            password=None,
            grpc_options=None
    ):
        """

        :param host:
        :param port:
        :param ca_cert:
        :param cert_key:
        :param cert_cert:
        :param timeout:
        :param user:
        :param password:
        :param grpc_options:
        """
        self._host = host
        self._port = port
        self._ca_cert = ca_cert
        self._cert_key = cert_key
        self._cert_cert = cert_cert
        self._timeout = timeout
        self._user = user
        self._password = password
        self._grpc_options = grpc_options
        self._cli: t.Optional[etcd3.client] = None
        self._lease_info: t.Optional[t.Dict] = {}

    def conn(self, typ: EtcdConnType):
        if typ == EtcdConnType.HTTP:
            self._cli = etcd3.client(
                host=self._host,
                port=self._port,
                ca_cert=self._ca_cert,
                cert_key=self._cert_key,
                cert_cert=self._cert_cert,
                timeout=self._timeout,
                user=self._user,
                password=self._password
            )
        elif typ == EtcdConnType.GRPC:
            self._cli = etcd3.client(
                ca_cert=self._ca_cert,
                cert_key=self._cert_key,
                cert_cert=self._cert_cert,
                timeout=self._timeout,
                user=self._user,
                password=self._password,
                grpc_options=self._grpc_options
            )
        else:
            self._cli = etcd3.client(
                host=self._host,
                port=self._port,
                ca_cert=self._ca_cert,
                cert_key=self._cert_key,
                cert_cert=self._cert_cert,
                timeout=self._timeout,
                user=self._user,
                password=self._password
            )

    def close(self):
        self._cli.close()

    def get(self, key: str):
        return self._cli.get(key)

    def get_prefix(self, key_prefix: str, **kwargs) -> t.Tuple:
        """
        Get a range of keys with a prefix.

        :param key_prefix: first key in range

        :returns: sequence of (value, metadata) tuples
        """
        return self._cli.get_prefix(key_prefix, **kwargs)

    def get_range(self, range_start: str, range_end: str, **kwargs):
        """
        Get a range of keys.

        :param range_start: first key in range
        :param range_end: last key in range
        :returns: sequence of (value, metadata) tuples
        """
        return self._cli.get_range(range_start, range_end, **kwargs)

    def put(self, key, value, lease=None, prev_kv=False):
        """
        Save a value to etcd.

        Example usage:

        .. code-block:: python

            >>> import etcd3
            >>> etcd = etcd3.client()
            >>> etcd.put('/thing/key', 'hello world')

        :param key: key in etcd to set
        :param value: value to set key to
        :type value: bytes
        :param lease: Lease to associate with this key.
        :type lease: either :class:`.Lease`, or int (ID of lease)
        :param prev_kv: return the previous key-value pair
        :type prev_kv: bool
        :returns: a response containing a header and the prev_kv
        :rtype: :class:`.rpc_pb2.PutResponse`
        """
        return self._cli.put(key, value, lease=lease, prev_kv=prev_kv)

    def put_nx(self, key, value, lease=None) -> bool:
        """
        Atomically puts a value only if the key previously had no value.

        This is the etcdv3 equivalent to setting a key with the etcdv2
        parameter prevExist=false.

        :param key: key in etcd to put
        :param value: value to be written to key
        :type value: bytes
        :param lease: Lease to associate with this key.
        :type lease: either :class:`.Lease`, or int (ID of lease)
        :returns: state of transaction, ``True`` if the put was successful,
                  ``False`` otherwise
        :rtype: bool
        """
        return self._cli.put_if_not_exists(key, value, lease=lease)

    def replace(self, key: str, initial_value, new_value) -> bool:
        """
        Atomically replace the value of a key with a new value.

        This compares the current value of a key, then replaces it with a new
        value if it is equal to a specified value. This operation takes place
        in a transaction.

        :param key: key in etcd to replace
        :param initial_value: old value to replace
        :type initial_value: bytes
        :param new_value: new value of the key
        :type new_value: bytes
        :returns: status of transaction, ``True`` if the replace was
                  successful, ``False`` otherwise
        :rtype: bool
        """
        return self._cli.replace(key, initial_value, new_value)

    def delete(self, key, prev_kv=False, return_response=False) -> bool:
        """
        Delete a single key in etcd.

        :param key: key in etcd to delete
        :param prev_kv: return the deleted key-value pair
        :type prev_kv: bool
        :param return_response: return the full response
        :type return_response: bool
        :returns: True if the key has been deleted when
                  ``return_response`` is False and a response containing
                  a header, the number of deleted keys and prev_kvs when
                  ``return_response`` is True
        """
        return self._cli.delete(key, prev_kv=prev_kv, return_response=return_response)

    def status(self):
        """Get the status of the responding member."""
        return self._cli.status()

    def watch(self, key: str, prefix_key=False, **kwargs):
        """
        Watch a range of keys with a prefix.

        :param key: key to watch

        :param prefix_key: is prefix key or not

        :returns: tuple of ``events_iterator`` and ``cancel``.
        """
        if prefix_key:
            return self._cli.watch_prefix(key, **kwargs)

        return self._cli.watch(key, **kwargs)

    def lease(self, ttl: int, lease_id=None):
        """
        Create a new lease.

        All keys attached to this lease will be expired and deleted if the
        lease expires. A lease can be sent keep alive messages to refresh the
        ttl.

        :param ttl: Requested time to live
        :param lease_id: Requested ID for the lease

        :returns: new lease
        :rtype: :class:`.Lease`
        """
        return self._cli.lease(ttl, lease_id=lease_id)

    def revoke_lease(self, lease_id: int):
        """
        Revoke a lease.

        :param lease_id: ID of the lease to revoke.
        """
        job_id = self._lease_info.get(lease_id)
        if job_id:
            # 1. 删除job
            apscheduler.cli.remove_job(job_id)

            # 2. 删除lease_info
            del self._lease_info[lease_id]

        return self._cli.revoke_lease(lease_id)

    def refresh_lease(self, lease_id: int):
        """

        :param lease_id:
        :return:
        """
        logging.info(f'start refresh lease {lease_id}...')

        response = self._cli.refresh_lease(lease_id)
        for resp in response:
            logging.debug(resp)

        logging.info(f'lease {lease_id} refresh success')

    def lease_keepalive(self, lease_id: int, interval: int):
        """

        :param lease_id:
        :param interval:
        :return:
        """
        job_id = f'registration-center-{lease_id}-keepalive'
        self._lease_info[lease_id] = job_id

        # 添加一个定时器, keepalive lease
        apscheduler.cli.add_job(
            id=job_id,
            func=self.refresh_lease,
            args=(lease_id,),
            trigger='interval',
            seconds=interval
        )

    def lock(self, name: str, ttl=60):
        """
        Create a new lock.

        :param name: name of the lock
        :type name: string or bytes
        :param ttl: length of time for the lock to live for in seconds. The
                    lock will be released after this time elapses, unless
                    refreshed
        :type ttl: int
        :returns: new lock
        :rtype: :class:`.Lock`
        """
        return self._cli.lock(name, ttl=ttl)


def new_client(
        host: str = 'localhost',
        port: int = 2379,
        grpc_options=None
) -> Client:
    return Client(host=host, port=port, grpc_options=grpc_options)