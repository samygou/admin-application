#!/usr/bin/python
# encoding: utf-8
"""
@Author: Samy
@File: __init__.py.py
@Time: 2022/2/22
@desc: 
"""
__all__ = ['ExceptionCode', 'APIException']

from . import define, exception

ExceptionCode = define.ExceptionCode
APIException = exception.APIException
