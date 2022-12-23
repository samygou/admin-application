import logging

from flask_sqlalchemy import SQLAlchemy

from application.exception import APIException, ExceptionCode


db = SQLAlchemy()


class DBSession:
    """db context manager"""
    def __init__(self, _db: SQLAlchemy):
        """

        :param _db:
        """
        self._db = _db

    def __enter__(self):
        return self._db.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self._db.session.commit()
        except Exception as e:
            logging.error(f'db session commit failed: {e}')
            self._db.session.rollback()
            raise APIException(
                ExceptionCode.INTERNAL_ERR_CODE,
                'server_err',
                'db commit failed'
            )
