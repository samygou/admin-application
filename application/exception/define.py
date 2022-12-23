#!/usr/bin/python
# encoding: utf-8
"""
@Author: Samy
@File: define.py
@Time: 2022/12/8
@desc: 
"""


class ExceptionCode:
    SUCCESS = 0                          # 成功
    UNKNOWN_CODE = 10000                 # 未知错误
    UNAUTH_CODE = 10001                  # 没有授权, 或者授权不被认可
    INVALID_PARAMS_CODE = 10002          # 参数错误
    PERMISSION_DENIED_CODE = 10003       # 没有授权
    NOT_FOUND_CODE = 10004               # 目标未找到
    ALREADY_EXIST_CODE = 10005           # 目标已经存在
    REQ_CANCELED_CODE = 10006            # 请求被取消
    DEADLINE_EXCEEDED_CODE = 10007       # 过期
    RESOURCE_EXHAUSTED_CODE = 10008      # 资源耗尽
    PRECONDITION_FAILED_CODE = 10009     # 前提条件故障
    ABORTED_CODE = 10010                 # 断言
    OUT_OF_RANGE_CODE = 10011            # 超过范围
    UNIMPLEMENTED_CODE = 10012           # 未被实现
    INTERNAL_ERR_CODE = 10013            # 内部错误
    UNAVAILABLE_CODE = 10014             # 对象不可用
    DATA_LOSS_CODE = 10015               # 数据丢失
