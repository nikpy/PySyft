# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/python/tuple.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.core.store import (
    store_object_pb2 as proto_dot_core_dot_store_dot_store__object__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/python/tuple.proto",
    package="syft.lib.python",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1cproto/lib/python/tuple.proto\x12\x0fsyft.lib.python\x1a%proto/core/common/common_object.proto\x1a#proto/core/store/store_object.proto"Y\n\x05Tuple\x12-\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x1f.syft.core.store.StorableObject\x12!\n\x02id\x18\x02 \x01(\x0b\x32\x15.syft.core.common.UIDb\x06proto3',
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
        proto_dot_core_dot_store_dot_store__object__pb2.DESCRIPTOR,
    ],
)


_TUPLE = _descriptor.Descriptor(
    name="Tuple",
    full_name="syft.lib.python.Tuple",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="data",
            full_name="syft.lib.python.Tuple.data",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="id",
            full_name="syft.lib.python.Tuple.id",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=125,
    serialized_end=214,
)

_TUPLE.fields_by_name[
    "data"
].message_type = proto_dot_core_dot_store_dot_store__object__pb2._STORABLEOBJECT
_TUPLE.fields_by_name[
    "id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
DESCRIPTOR.message_types_by_name["Tuple"] = _TUPLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Tuple = _reflection.GeneratedProtocolMessageType(
    "Tuple",
    (_message.Message,),
    {
        "DESCRIPTOR": _TUPLE,
        "__module__": "proto.lib.python.tuple_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.python.Tuple)
    },
)
_sym_db.RegisterMessage(Tuple)


# @@protoc_insertion_point(module_scope)
