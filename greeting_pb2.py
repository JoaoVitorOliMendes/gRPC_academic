# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: greeting.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'greeting.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0egreeting.proto\"$\n\x0cGreetRequest\x12\x14\n\x0cgreetMessage\x18\x01 \x01(\t\" \n\rGreetResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2:\n\x10GreetingServicer\x12&\n\x05Greet\x12\r.GreetRequest\x1a\x0e.GreetResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'greeting_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GREETREQUEST']._serialized_start=18
  _globals['_GREETREQUEST']._serialized_end=54
  _globals['_GREETRESPONSE']._serialized_start=56
  _globals['_GREETRESPONSE']._serialized_end=88
  _globals['_GREETINGSERVICER']._serialized_start=90
  _globals['_GREETINGSERVICER']._serialized_end=148
# @@protoc_insertion_point(module_scope)
