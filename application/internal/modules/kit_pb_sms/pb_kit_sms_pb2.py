# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pb_kit_sms.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pb_kit_sms.proto',
  package='pb_kit_sm',
  syntax='proto3',
  serialized_options=b'Z2git.aimall-tech.com/product/infra/api/pb/pb_kit_sm',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10pb_kit_sms.proto\x12\tpb_kit_sm\"8\n\tSendSMReq\x12\r\n\x05phone\x18\x01 \x01(\t\x12\x0b\n\x03typ\x18\x02 \x01(\t\x12\x0f\n\x07\x65xpired\x18\x03 \x01(\x03\":\n\nSendSMResp\x12\x1d\n\x03\x65rr\x18\x01 \x01(\x0e\x32\x10.pb_kit_sm.Error\x12\r\n\x05token\x18\x02 \x01(\t\"\xce\x01\n\x11SendTemplateSMReq\x12\r\n\x05phone\x18\x01 \x01(\t\x12\x11\n\tsign_name\x18\x02 \x01(\t\x12\x15\n\rtemplate_code\x18\x03 \x01(\t\x12I\n\x0ftemplate_params\x18\x04 \x03(\x0b\x32\x30.pb_kit_sm.SendTemplateSMReq.TemplateParamsEntry\x1a\x35\n\x13TemplateParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"3\n\x12SendTemplateSMResp\x12\x1d\n\x03\x65rr\x18\x01 \x01(\x0e\x32\x10.pb_kit_sm.Error\":\n\x0c\x43heckCodeReq\x12\r\n\x05phone\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t\".\n\rCheckCodeResp\x12\x1d\n\x03\x65rr\x18\x01 \x01(\x0e\x32\x10.pb_kit_sm.Error*\x81\x01\n\x05\x45rror\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x46\x61ult\x10\x01\x12\x15\n\x11OutOfLimitControl\x10\x02\x12\x19\n\x15SendFailUnknownReason\x10\x03\x12\x0f\n\x0bInvalidCode\x10\x04\x12\x10\n\x0cInvalidToken\x10\x05\x12\x10\n\x0cTokenExpired\x10\x06\x32\xd1\x01\n\x03\x41PI\x12\x37\n\x06SendSM\x12\x14.pb_kit_sm.SendSMReq\x1a\x15.pb_kit_sm.SendSMResp\"\x00\x12@\n\tCheckCode\x12\x17.pb_kit_sm.CheckCodeReq\x1a\x18.pb_kit_sm.CheckCodeResp\"\x00\x12O\n\x0eSendTemplateSM\x12\x1c.pb_kit_sm.SendTemplateSMReq\x1a\x1d.pb_kit_sm.SendTemplateSMResp\"\x00\x42\x34Z2git.aimall-tech.com/product/infra/api/pb/pb_kit_smb\x06proto3'
)

_ERROR = _descriptor.EnumDescriptor(
  name='Error',
  full_name='pb_kit_sm.Error',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Fault', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OutOfLimitControl', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SendFailUnknownReason', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='InvalidCode', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='InvalidToken', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TokenExpired', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=520,
  serialized_end=649,
)
_sym_db.RegisterEnumDescriptor(_ERROR)

Error = enum_type_wrapper.EnumTypeWrapper(_ERROR)
OK = 0
Fault = 1
OutOfLimitControl = 2
SendFailUnknownReason = 3
InvalidCode = 4
InvalidToken = 5
TokenExpired = 6



_SENDSMREQ = _descriptor.Descriptor(
  name='SendSMReq',
  full_name='pb_kit_sm.SendSMReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone', full_name='pb_kit_sm.SendSMReq.phone', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='typ', full_name='pb_kit_sm.SendSMReq.typ', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expired', full_name='pb_kit_sm.SendSMReq.expired', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=87,
)


_SENDSMRESP = _descriptor.Descriptor(
  name='SendSMResp',
  full_name='pb_kit_sm.SendSMResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='pb_kit_sm.SendSMResp.err', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='pb_kit_sm.SendSMResp.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=147,
)


_SENDTEMPLATESMREQ_TEMPLATEPARAMSENTRY = _descriptor.Descriptor(
  name='TemplateParamsEntry',
  full_name='pb_kit_sm.SendTemplateSMReq.TemplateParamsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pb_kit_sm.SendTemplateSMReq.TemplateParamsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='pb_kit_sm.SendTemplateSMReq.TemplateParamsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=356,
)

_SENDTEMPLATESMREQ = _descriptor.Descriptor(
  name='SendTemplateSMReq',
  full_name='pb_kit_sm.SendTemplateSMReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone', full_name='pb_kit_sm.SendTemplateSMReq.phone', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sign_name', full_name='pb_kit_sm.SendTemplateSMReq.sign_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='template_code', full_name='pb_kit_sm.SendTemplateSMReq.template_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='template_params', full_name='pb_kit_sm.SendTemplateSMReq.template_params', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SENDTEMPLATESMREQ_TEMPLATEPARAMSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=356,
)


_SENDTEMPLATESMRESP = _descriptor.Descriptor(
  name='SendTemplateSMResp',
  full_name='pb_kit_sm.SendTemplateSMResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='pb_kit_sm.SendTemplateSMResp.err', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=358,
  serialized_end=409,
)


_CHECKCODEREQ = _descriptor.Descriptor(
  name='CheckCodeReq',
  full_name='pb_kit_sm.CheckCodeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone', full_name='pb_kit_sm.CheckCodeReq.phone', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='pb_kit_sm.CheckCodeReq.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='pb_kit_sm.CheckCodeReq.token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=411,
  serialized_end=469,
)


_CHECKCODERESP = _descriptor.Descriptor(
  name='CheckCodeResp',
  full_name='pb_kit_sm.CheckCodeResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='err', full_name='pb_kit_sm.CheckCodeResp.err', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=471,
  serialized_end=517,
)

_SENDSMRESP.fields_by_name['err'].enum_type = _ERROR
_SENDTEMPLATESMREQ_TEMPLATEPARAMSENTRY.containing_type = _SENDTEMPLATESMREQ
_SENDTEMPLATESMREQ.fields_by_name['template_params'].message_type = _SENDTEMPLATESMREQ_TEMPLATEPARAMSENTRY
_SENDTEMPLATESMRESP.fields_by_name['err'].enum_type = _ERROR
_CHECKCODERESP.fields_by_name['err'].enum_type = _ERROR
DESCRIPTOR.message_types_by_name['SendSMReq'] = _SENDSMREQ
DESCRIPTOR.message_types_by_name['SendSMResp'] = _SENDSMRESP
DESCRIPTOR.message_types_by_name['SendTemplateSMReq'] = _SENDTEMPLATESMREQ
DESCRIPTOR.message_types_by_name['SendTemplateSMResp'] = _SENDTEMPLATESMRESP
DESCRIPTOR.message_types_by_name['CheckCodeReq'] = _CHECKCODEREQ
DESCRIPTOR.message_types_by_name['CheckCodeResp'] = _CHECKCODERESP
DESCRIPTOR.enum_types_by_name['Error'] = _ERROR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendSMReq = _reflection.GeneratedProtocolMessageType('SendSMReq', (_message.Message,), {
  'DESCRIPTOR' : _SENDSMREQ,
  '__module__' : 'pb_kit_sms_pb2'
  # @@protoc_insertion_point(class_scope:pb_kit_sm.SendSMReq)
  })
_sym_db.RegisterMessage(SendSMReq)

SendSMResp = _reflection.GeneratedProtocolMessageType('SendSMResp', (_message.Message,), {
  'DESCRIPTOR' : _SENDSMRESP,
  '__module__' : 'pb_kit_sms_pb2'
  # @@protoc_insertion_point(class_scope:pb_kit_sm.SendSMResp)
  })
_sym_db.RegisterMessage(SendSMResp)

SendTemplateSMReq = _reflection.GeneratedProtocolMessageType('SendTemplateSMReq', (_message.Message,), {

  'TemplateParamsEntry' : _reflection.GeneratedProtocolMessageType('TemplateParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SENDTEMPLATESMREQ_TEMPLATEPARAMSENTRY,
    '__module__' : 'pb_kit_sms_pb2'
    # @@protoc_insertion_point(class_scope:pb_kit_sm.SendTemplateSMReq.TemplateParamsEntry)
    })
  ,
  'DESCRIPTOR' : _SENDTEMPLATESMREQ,
  '__module__' : 'pb_kit_sms_pb2'
  # @@protoc_insertion_point(class_scope:pb_kit_sm.SendTemplateSMReq)
  })
_sym_db.RegisterMessage(SendTemplateSMReq)
_sym_db.RegisterMessage(SendTemplateSMReq.TemplateParamsEntry)

SendTemplateSMResp = _reflection.GeneratedProtocolMessageType('SendTemplateSMResp', (_message.Message,), {
  'DESCRIPTOR' : _SENDTEMPLATESMRESP,
  '__module__' : 'pb_kit_sms_pb2'
  # @@protoc_insertion_point(class_scope:pb_kit_sm.SendTemplateSMResp)
  })
_sym_db.RegisterMessage(SendTemplateSMResp)

CheckCodeReq = _reflection.GeneratedProtocolMessageType('CheckCodeReq', (_message.Message,), {
  'DESCRIPTOR' : _CHECKCODEREQ,
  '__module__' : 'pb_kit_sms_pb2'
  # @@protoc_insertion_point(class_scope:pb_kit_sm.CheckCodeReq)
  })
_sym_db.RegisterMessage(CheckCodeReq)

CheckCodeResp = _reflection.GeneratedProtocolMessageType('CheckCodeResp', (_message.Message,), {
  'DESCRIPTOR' : _CHECKCODERESP,
  '__module__' : 'pb_kit_sms_pb2'
  # @@protoc_insertion_point(class_scope:pb_kit_sm.CheckCodeResp)
  })
_sym_db.RegisterMessage(CheckCodeResp)


DESCRIPTOR._options = None
_SENDTEMPLATESMREQ_TEMPLATEPARAMSENTRY._options = None

_API = _descriptor.ServiceDescriptor(
  name='API',
  full_name='pb_kit_sm.API',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=652,
  serialized_end=861,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendSM',
    full_name='pb_kit_sm.API.SendSM',
    index=0,
    containing_service=None,
    input_type=_SENDSMREQ,
    output_type=_SENDSMRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CheckCode',
    full_name='pb_kit_sm.API.CheckCode',
    index=1,
    containing_service=None,
    input_type=_CHECKCODEREQ,
    output_type=_CHECKCODERESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendTemplateSM',
    full_name='pb_kit_sm.API.SendTemplateSM',
    index=2,
    containing_service=None,
    input_type=_SENDTEMPLATESMREQ,
    output_type=_SENDTEMPLATESMRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_API)

DESCRIPTOR.services_by_name['API'] = _API

# @@protoc_insertion_point(module_scope)
