#!/usr/bin/python
# encoding: utf-8
"""
@Author: Samy
@File: response.py
@Time: 2022/2/22
@desc: 
"""
import typing as t

from application.exception import ExceptionCode


class ResponseHandler:
    @staticmethod
    def process(
            code: int = ExceptionCode.UNKNOWN_CODE,
            name: str = 'unknown_error',
            desc: str = '未知错误',
            **kwargs
    ) -> t.Dict[str, t.Any]:
        return dict(code=code, err_name=name, err_desc=desc, **kwargs)
