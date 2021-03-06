# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: payload.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='payload.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\rpayload.proto\"\xc1\x01\n\x13SimpleSupplyPayload\x12+\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x1b.SimpleSupplyPayload.Action\x12*\n\x10synchronize_data\x18\x02 \x01(\x0b\x32\x10.SynchronizeData\x12 \n\x0b\x63reate_user\x18\x03 \x01(\x0b\x32\x0b.CreateUser\"/\n\x06\x41\x63tion\x12\x14\n\x10SYNCHRONIZE_DATA\x10\x00\x12\x0f\n\x0b\x43REATE_USER\x10\x01\"\x1f\n\x0fSynchronizeData\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"-\n\nCreateUser\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\tb\x06proto3'
)



_SIMPLESUPPLYPAYLOAD_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='SimpleSupplyPayload.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SYNCHRONIZE_DATA', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATE_USER', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=164,
  serialized_end=211,
)
_sym_db.RegisterEnumDescriptor(_SIMPLESUPPLYPAYLOAD_ACTION)


_SIMPLESUPPLYPAYLOAD = _descriptor.Descriptor(
  name='SimpleSupplyPayload',
  full_name='SimpleSupplyPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='SimpleSupplyPayload.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='synchronize_data', full_name='SimpleSupplyPayload.synchronize_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_user', full_name='SimpleSupplyPayload.create_user', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SIMPLESUPPLYPAYLOAD_ACTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=211,
)


_SYNCHRONIZEDATA = _descriptor.Descriptor(
  name='SynchronizeData',
  full_name='SynchronizeData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='SynchronizeData.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=213,
  serialized_end=244,
)


_CREATEUSER = _descriptor.Descriptor(
  name='CreateUser',
  full_name='CreateUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='CreateUser.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='CreateUser.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=246,
  serialized_end=291,
)

_SIMPLESUPPLYPAYLOAD.fields_by_name['action'].enum_type = _SIMPLESUPPLYPAYLOAD_ACTION
_SIMPLESUPPLYPAYLOAD.fields_by_name['synchronize_data'].message_type = _SYNCHRONIZEDATA
_SIMPLESUPPLYPAYLOAD.fields_by_name['create_user'].message_type = _CREATEUSER
_SIMPLESUPPLYPAYLOAD_ACTION.containing_type = _SIMPLESUPPLYPAYLOAD
DESCRIPTOR.message_types_by_name['SimpleSupplyPayload'] = _SIMPLESUPPLYPAYLOAD
DESCRIPTOR.message_types_by_name['SynchronizeData'] = _SYNCHRONIZEDATA
DESCRIPTOR.message_types_by_name['CreateUser'] = _CREATEUSER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimpleSupplyPayload = _reflection.GeneratedProtocolMessageType('SimpleSupplyPayload', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLESUPPLYPAYLOAD,
  '__module__' : 'payload_pb2'
  # @@protoc_insertion_point(class_scope:SimpleSupplyPayload)
  })
_sym_db.RegisterMessage(SimpleSupplyPayload)

SynchronizeData = _reflection.GeneratedProtocolMessageType('SynchronizeData', (_message.Message,), {
  'DESCRIPTOR' : _SYNCHRONIZEDATA,
  '__module__' : 'payload_pb2'
  # @@protoc_insertion_point(class_scope:SynchronizeData)
  })
_sym_db.RegisterMessage(SynchronizeData)

CreateUser = _reflection.GeneratedProtocolMessageType('CreateUser', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSER,
  '__module__' : 'payload_pb2'
  # @@protoc_insertion_point(class_scope:CreateUser)
  })
_sym_db.RegisterMessage(CreateUser)


# @@protoc_insertion_point(module_scope)
