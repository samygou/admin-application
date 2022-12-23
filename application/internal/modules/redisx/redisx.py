import logging
import typing as t
import threading
import uuid

from flask_redis import FlaskRedis

from application.internal.modules.utils import Singleton


_MAX_CONNECTIONS = 20


class Client(Singleton):
    """redis client"""

    def __init__(
            self,
            username: str = None,
            password: int = None,
            db: int = 0,
            max_connections: int = 20,
            decode_responses: bool = True
    ):
        self._params = {'db': db, 'max_connections': max_connections, 'decode_responses': decode_responses}
        if username:
            self._params['username'] = username
        if password:
            self._params['password'] = password
        self.cli: FlaskRedis = FlaskRedis(**self._params)

    def ping(self) -> bool:
        """

        :return:
        """
        return self.cli.ping()

    def keep_alive(self):
        """

        :return:
        """
        timer = threading.Timer(30.0, self.ping)
        timer.start()

    def set(self, name: str, val: t.Any):
        """"""

    def lock(self, lock_name: str, expired: int = 60):
        """
        redis distributed lock
        :param lock_name: lock name
        :param expired:
        :return:
        """
        return _Lock(lock_name, ttl=expired, client=self)


class _Lock:
    """分布式锁"""

    def __init__(
            self,
            name: str,
            ttl: int = 60,
            client: t.Optional[Client] = None
    ):
        """

        :param name:
        :param ttl:
        """
        self._name = name
        self._val = uuid.uuid4().bytes
        self._ttl = ttl
        self.redis_cli = client

    def acquire(self):
        if self.redis_cli.cli.set(self._name, self._val, ex=self._ttl, nx=True):
            if self.redis_cli.cli.ttl(self._name) == -1:
                self.redis_cli.cli.expired(self._name, self._ttl)

            return True

        return False

    def release(self):
        self.redis_cli.cli.delete(self._name)

    def is_acquired(self) -> bool:
        val = self.redis_cli.cli.get(self._name)

        if not val:
            return False

        return val == self._val

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()


def new_client(
        db: int = 0,
        username: str = None,
        password: str = None,
        max_connections: int = _MAX_CONNECTIONS,
        decode_responses: bool = False
) -> Client:
    return Client(
        username=username,
        password=password,
        db=db,
        max_connections=max_connections,
        decode_responses=decode_responses
    )
