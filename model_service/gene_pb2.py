# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: gene.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'gene.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ngene.proto\x12\x12mutationprediction\"-\n\x16PredictMutationRequest\x12\x13\n\x0b\x66naFileData\x18\x01 \x01(\x0c\"+\n\x14PredictMutationReply\x12\x13\n\x0bpredictions\x18\x01 \x03(\x02\x32\x86\x01\n\x19MutationPredictionService\x12i\n\x0fPredictMutation\x12*.mutationprediction.PredictMutationRequest\x1a(.mutationprediction.PredictMutationReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gene_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PREDICTMUTATIONREQUEST']._serialized_start=34
  _globals['_PREDICTMUTATIONREQUEST']._serialized_end=79
  _globals['_PREDICTMUTATIONREPLY']._serialized_start=81
  _globals['_PREDICTMUTATIONREPLY']._serialized_end=124
  _globals['_MUTATIONPREDICTIONSERVICE']._serialized_start=127
  _globals['_MUTATIONPREDICTIONSERVICE']._serialized_end=261
# @@protoc_insertion_point(module_scope)
