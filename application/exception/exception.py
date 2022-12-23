#!/usr/bin/python
# encoding: utf-8
"""
@Author: Samy
@File: exception.py
@Time: 2022/12/9
@desc: 
"""
import typing as t

from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    """API异常捕获"""
    def __init__(self, code: int = None, err_name: str = None, err_desc: str = None, status_code: int = None):
        """
        :param code: 自定义的code码
        :param err_name: 错误名
        :param err_desc: 错误描述
        :param status_code: http的code码, 用于自定义http code码
        """
        self.code = code if code else 10001
        self.err_name = err_name if err_name else 'unknown_error'
        self.err_desc = err_desc if err_desc else '未知错误'
        self.status_code = status_code

    def to_dict(self) -> t.Dict[str, t.Any]:
        result = {
            'code': self.code,
            'err_name': self.err_name,
            'err_desc': self.err_desc,
        }

        # 用于改变http status code码
        if self.status_code:
            result['status_code'] = self.status_code

        return result
