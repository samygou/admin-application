from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ACCOUNT_NOT_EXIST: Error
DESCRIPTOR: _descriptor.FileDescriptor
OK: Error
SERVER_FAULT: Error

class Account(_message.Message):
    __slots__ = ["name", "phone", "remark", "uid"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    REMARK_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    name: str
    phone: str
    remark: str
    uid: str
    def __init__(self, uid: _Optional[str] = ..., name: _Optional[str] = ..., phone: _Optional[str] = ..., remark: _Optional[str] = ...) -> None: ...

class Company(_message.Message):
    __slots__ = ["config", "expired", "modules", "name", "uid"]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_FIELD_NUMBER: _ClassVar[int]
    MODULES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    config: CompanyConfig
    expired: int
    modules: _containers.RepeatedScalarFieldContainer[str]
    name: str
    uid: str
    def __init__(self, uid: _Optional[str] = ..., name: _Optional[str] = ..., modules: _Optional[_Iterable[str]] = ..., expired: _Optional[int] = ..., config: _Optional[_Union[CompanyConfig, _Mapping]] = ...) -> None: ...

class CompanyConfig(_message.Message):
    __slots__ = ["algConfig"]
    class AlgConfig(_message.Message):
        __slots__ = ["inventory"]
        INVENTORY_FIELD_NUMBER: _ClassVar[int]
        inventory: str
        def __init__(self, inventory: _Optional[str] = ...) -> None: ...
    ALGCONFIG_FIELD_NUMBER: _ClassVar[int]
    algConfig: CompanyConfig.AlgConfig
    def __init__(self, algConfig: _Optional[_Union[CompanyConfig.AlgConfig, _Mapping]] = ...) -> None: ...

class GetAccountByPhoneReply(_message.Message):
    __slots__ = ["account", "err"]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ERR_FIELD_NUMBER: _ClassVar[int]
    account: Account
    err: Error
    def __init__(self, err: _Optional[_Union[Error, str]] = ..., account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class GetAccountByPhoneReq(_message.Message):
    __slots__ = ["phone"]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    phone: str
    def __init__(self, phone: _Optional[str] = ...) -> None: ...

class GetAccountByUIDReply(_message.Message):
    __slots__ = ["account", "err"]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ERR_FIELD_NUMBER: _ClassVar[int]
    account: Account
    err: Error
    def __init__(self, err: _Optional[_Union[Error, str]] = ..., account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class GetAccountByUIDReq(_message.Message):
    __slots__ = ["uid"]
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    def __init__(self, uid: _Optional[str] = ...) -> None: ...

class ListCompaniesByUidReq(_message.Message):
    __slots__ = ["uid"]
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uid: _Optional[_Iterable[str]] = ...) -> None: ...

class ListCompaniesReply(_message.Message):
    __slots__ = ["companies", "err"]
    COMPANIES_FIELD_NUMBER: _ClassVar[int]
    ERR_FIELD_NUMBER: _ClassVar[int]
    companies: _containers.RepeatedCompositeFieldContainer[Company]
    err: Error
    def __init__(self, err: _Optional[_Union[Error, str]] = ..., companies: _Optional[_Iterable[_Union[Company, _Mapping]]] = ...) -> None: ...

class ListCompaniesReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Error(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
