# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rrequest.proto\x12\x0bintelligent\"M\n\x04Lamp\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x08\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\r\n\x05\x63olor\x18\x04 \x01(\t\x12\x0c\n\x04\x63mds\x18\x05 \x03(\t\"^\n\tTreadmill\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x08\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0c\n\x04\x64ist\x18\x04 \x01(\x01\x12\x0b\n\x03vel\x18\x05 \x01(\x02\x12\x0c\n\x04\x63mds\x18\x06 \x03(\t\"J\n\x02\x41\x43\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x08\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0c\n\x04temp\x18\x04 \x01(\x05\x12\x0c\n\x04\x63mds\x18\x05 \x03(\t\"v\n\x08Response\x12 \n\x05lamps\x18\x01 \x03(\x0b\x32\x11.intelligent.Lamp\x12*\n\ntreadmills\x18\x02 \x03(\x0b\x32\x16.intelligent.Treadmill\x12\x1c\n\x03\x61\x63s\x18\x03 \x03(\x0b\x32\x0f.intelligent.AC\"B\n\x07Request\x12\x0b\n\x03\x63md\x18\x01 \x01(\t\x12\x0e\n\x06id_obj\x18\x02 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x03(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\"\x99\x01\n\x14ResponseSingleObject\x12\x0e\n\x06id_obj\x18\x01 \x01(\t\x12!\n\x04objL\x18\x02 \x01(\x0b\x32\x11.intelligent.LampH\x00\x12&\n\x04objT\x18\x03 \x01(\x0b\x32\x16.intelligent.TreadmillH\x00\x12\x1f\n\x04objA\x18\x04 \x01(\x0b\x32\x0f.intelligent.ACH\x00\x42\x05\n\x03obj\">\n\x0cResponseLamp\x12\x0e\n\x06id_obj\x18\x01 \x01(\t\x12\x1e\n\x03obj\x18\x02 \x01(\x0b\x32\x11.intelligent.Lamp\"H\n\x11ResponseTreadmill\x12\x0e\n\x06id_obj\x18\x01 \x01(\t\x12#\n\x03obj\x18\x02 \x01(\x0b\x32\x16.intelligent.Treadmill\":\n\nResponseAC\x12\x0e\n\x06id_obj\x18\x01 \x01(\t\x12\x1c\n\x03obj\x18\x02 \x01(\x0b\x32\x0f.intelligent.ACb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'request_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LAMP._serialized_start=30
  _LAMP._serialized_end=107
  _TREADMILL._serialized_start=109
  _TREADMILL._serialized_end=203
  _AC._serialized_start=205
  _AC._serialized_end=279
  _RESPONSE._serialized_start=281
  _RESPONSE._serialized_end=399
  _REQUEST._serialized_start=401
  _REQUEST._serialized_end=467
  _RESPONSESINGLEOBJECT._serialized_start=470
  _RESPONSESINGLEOBJECT._serialized_end=623
  _RESPONSELAMP._serialized_start=625
  _RESPONSELAMP._serialized_end=687
  _RESPONSETREADMILL._serialized_start=689
  _RESPONSETREADMILL._serialized_end=761
  _RESPONSEAC._serialized_start=763
  _RESPONSEAC._serialized_end=821
# @@protoc_insertion_point(module_scope)
