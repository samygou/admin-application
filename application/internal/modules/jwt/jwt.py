import typing as t
import logging
import traceback
import os

import jwt


def format_(
        payload: t.Dict[str, t.Any],
        key: str,
        algorithm: str = 'HS256',
        headers: t.Optional[t.Dict[str, t.Any]] = None
):
    """
    jwt encode
    :param payload:
    :param key:
    :param algorithm:
    :param headers:
    :return:
    """
    try:
        if 'salt' not in payload:
            payload['salt'] = os.urandom(16).hex()

        token = jwt.encode(
            payload=payload,
            key=key,
            algorithm=algorithm,
            headers=headers
        )
        return token
    except Exception as e:
        logging.error(e)
        traceback.print_exc()
        raise


def parse(
        token: str,
        key: str,
        algorithms: t.Optional[t.List[str]] = None
) -> t.Dict[str, t.Any]:
    """
    jwt decode
    :param token:
    :param key:
    :param algorithms:
    :return:
    """
    if algorithms is None:
        algorithms = ['HS256']
    try:
        payload = jwt.decode(token, key, algorithms=algorithms)
        return payload
    except Exception as e:
        logging.error(e)
        traceback.print_exc()
        raise
