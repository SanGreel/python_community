# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: library.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='library.proto',
  package='server',
  syntax='proto3',
  serialized_pb=_b('\n\rlibrary.proto\x12\x06server\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\"3\n\x04\x42ook\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\":\n\x0b\x42ookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\"\'\n\x08\x42ookList\x12\x1b\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\x0c.server.Book2\x96\x03\n\x07Library\x12L\n\tListBooks\x12\x16.google.protobuf.Empty\x1a\x10.server.BookList\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/api/v1/books\x12J\n\x07GetBook\x12\x13.server.BookRequest\x1a\x0c.server.Book\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/api/v1/books/{isbn}\x12\x46\n\x07\x41\x64\x64\x42ook\x12\x13.server.BookRequest\x1a\x0c.server.Book\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/api/v1/books:\x01*\x12P\n\nUpdateBook\x12\x13.server.BookRequest\x1a\x0c.server.Book\"\x1f\x82\xd3\xe4\x93\x02\x19\x1a\x14/api/v1/books/{isbn}:\x01*\x12W\n\nDeleteBook\x12\x13.server.BookRequest\x1a\x16.google.protobuf.Empty\"\x1c\x82\xd3\xe4\x93\x02\x16*\x14/api/v1/books/{isbn}b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_BOOK = _descriptor.Descriptor(
  name='Book',
  full_name='server.Book',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isbn', full_name='server.Book.isbn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='server.Book.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='author', full_name='server.Book.author', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=135,
)


_BOOKREQUEST = _descriptor.Descriptor(
  name='BookRequest',
  full_name='server.BookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isbn', full_name='server.BookRequest.isbn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='server.BookRequest.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='author', full_name='server.BookRequest.author', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=195,
)


_BOOKLIST = _descriptor.Descriptor(
  name='BookList',
  full_name='server.BookList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='books', full_name='server.BookList.books', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=236,
)

_BOOKLIST.fields_by_name['books'].message_type = _BOOK
DESCRIPTOR.message_types_by_name['Book'] = _BOOK
DESCRIPTOR.message_types_by_name['BookRequest'] = _BOOKREQUEST
DESCRIPTOR.message_types_by_name['BookList'] = _BOOKLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Book = _reflection.GeneratedProtocolMessageType('Book', (_message.Message,), dict(
  DESCRIPTOR = _BOOK,
  __module__ = 'library_pb2'
  # @@protoc_insertion_point(class_scope:server.Book)
  ))
_sym_db.RegisterMessage(Book)

BookRequest = _reflection.GeneratedProtocolMessageType('BookRequest', (_message.Message,), dict(
  DESCRIPTOR = _BOOKREQUEST,
  __module__ = 'library_pb2'
  # @@protoc_insertion_point(class_scope:server.BookRequest)
  ))
_sym_db.RegisterMessage(BookRequest)

BookList = _reflection.GeneratedProtocolMessageType('BookList', (_message.Message,), dict(
  DESCRIPTOR = _BOOKLIST,
  __module__ = 'library_pb2'
  # @@protoc_insertion_point(class_scope:server.BookList)
  ))
_sym_db.RegisterMessage(BookList)



_LIBRARY = _descriptor.ServiceDescriptor(
  name='Library',
  full_name='server.Library',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=239,
  serialized_end=645,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListBooks',
    full_name='server.Library.ListBooks',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_BOOKLIST,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\017\022\r/api/v1/books')),
  ),
  _descriptor.MethodDescriptor(
    name='GetBook',
    full_name='server.Library.GetBook',
    index=1,
    containing_service=None,
    input_type=_BOOKREQUEST,
    output_type=_BOOK,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\026\022\024/api/v1/books/{isbn}')),
  ),
  _descriptor.MethodDescriptor(
    name='AddBook',
    full_name='server.Library.AddBook',
    index=2,
    containing_service=None,
    input_type=_BOOKREQUEST,
    output_type=_BOOK,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\022\"\r/api/v1/books:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateBook',
    full_name='server.Library.UpdateBook',
    index=3,
    containing_service=None,
    input_type=_BOOKREQUEST,
    output_type=_BOOK,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\031\032\024/api/v1/books/{isbn}:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteBook',
    full_name='server.Library.DeleteBook',
    index=4,
    containing_service=None,
    input_type=_BOOKREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\026*\024/api/v1/books/{isbn}')),
  ),
])
_sym_db.RegisterServiceDescriptor(_LIBRARY)

DESCRIPTOR.services_by_name['Library'] = _LIBRARY

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class LibraryStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.ListBooks = channel.unary_unary(
          '/server.Library/ListBooks',
          request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
          response_deserializer=BookList.FromString,
          )
      self.GetBook = channel.unary_unary(
          '/server.Library/GetBook',
          request_serializer=BookRequest.SerializeToString,
          response_deserializer=Book.FromString,
          )
      self.AddBook = channel.unary_unary(
          '/server.Library/AddBook',
          request_serializer=BookRequest.SerializeToString,
          response_deserializer=Book.FromString,
          )
      self.UpdateBook = channel.unary_unary(
          '/server.Library/UpdateBook',
          request_serializer=BookRequest.SerializeToString,
          response_deserializer=Book.FromString,
          )
      self.DeleteBook = channel.unary_unary(
          '/server.Library/DeleteBook',
          request_serializer=BookRequest.SerializeToString,
          response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          )


  class LibraryServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def ListBooks(self, request, context):
      """ListBooks returns all Books
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetBook(self, request, context):
      """GetBook returns book by isbn
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def AddBook(self, request, context):
      """AddBook allows to add a book
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def UpdateBook(self, request, context):
      """UpdateBook allows to update a book
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def DeleteBook(self, request, context):
      """DeleteBook deletes book identified by isbn
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_LibraryServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'ListBooks': grpc.unary_unary_rpc_method_handler(
            servicer.ListBooks,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=BookList.SerializeToString,
        ),
        'GetBook': grpc.unary_unary_rpc_method_handler(
            servicer.GetBook,
            request_deserializer=BookRequest.FromString,
            response_serializer=Book.SerializeToString,
        ),
        'AddBook': grpc.unary_unary_rpc_method_handler(
            servicer.AddBook,
            request_deserializer=BookRequest.FromString,
            response_serializer=Book.SerializeToString,
        ),
        'UpdateBook': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateBook,
            request_deserializer=BookRequest.FromString,
            response_serializer=Book.SerializeToString,
        ),
        'DeleteBook': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteBook,
            request_deserializer=BookRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'server.Library', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaLibraryServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def ListBooks(self, request, context):
      """ListBooks returns all Books
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetBook(self, request, context):
      """GetBook returns book by isbn
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def AddBook(self, request, context):
      """AddBook allows to add a book
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def UpdateBook(self, request, context):
      """UpdateBook allows to update a book
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def DeleteBook(self, request, context):
      """DeleteBook deletes book identified by isbn
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaLibraryStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def ListBooks(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """ListBooks returns all Books
      """
      raise NotImplementedError()
    ListBooks.future = None
    def GetBook(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """GetBook returns book by isbn
      """
      raise NotImplementedError()
    GetBook.future = None
    def AddBook(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """AddBook allows to add a book
      """
      raise NotImplementedError()
    AddBook.future = None
    def UpdateBook(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """UpdateBook allows to update a book
      """
      raise NotImplementedError()
    UpdateBook.future = None
    def DeleteBook(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """DeleteBook deletes book identified by isbn
      """
      raise NotImplementedError()
    DeleteBook.future = None


  def beta_create_Library_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('server.Library', 'AddBook'): BookRequest.FromString,
      ('server.Library', 'DeleteBook'): BookRequest.FromString,
      ('server.Library', 'GetBook'): BookRequest.FromString,
      ('server.Library', 'ListBooks'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
      ('server.Library', 'UpdateBook'): BookRequest.FromString,
    }
    response_serializers = {
      ('server.Library', 'AddBook'): Book.SerializeToString,
      ('server.Library', 'DeleteBook'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ('server.Library', 'GetBook'): Book.SerializeToString,
      ('server.Library', 'ListBooks'): BookList.SerializeToString,
      ('server.Library', 'UpdateBook'): Book.SerializeToString,
    }
    method_implementations = {
      ('server.Library', 'AddBook'): face_utilities.unary_unary_inline(servicer.AddBook),
      ('server.Library', 'DeleteBook'): face_utilities.unary_unary_inline(servicer.DeleteBook),
      ('server.Library', 'GetBook'): face_utilities.unary_unary_inline(servicer.GetBook),
      ('server.Library', 'ListBooks'): face_utilities.unary_unary_inline(servicer.ListBooks),
      ('server.Library', 'UpdateBook'): face_utilities.unary_unary_inline(servicer.UpdateBook),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Library_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('server.Library', 'AddBook'): BookRequest.SerializeToString,
      ('server.Library', 'DeleteBook'): BookRequest.SerializeToString,
      ('server.Library', 'GetBook'): BookRequest.SerializeToString,
      ('server.Library', 'ListBooks'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ('server.Library', 'UpdateBook'): BookRequest.SerializeToString,
    }
    response_deserializers = {
      ('server.Library', 'AddBook'): Book.FromString,
      ('server.Library', 'DeleteBook'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
      ('server.Library', 'GetBook'): Book.FromString,
      ('server.Library', 'ListBooks'): BookList.FromString,
      ('server.Library', 'UpdateBook'): Book.FromString,
    }
    cardinalities = {
      'AddBook': cardinality.Cardinality.UNARY_UNARY,
      'DeleteBook': cardinality.Cardinality.UNARY_UNARY,
      'GetBook': cardinality.Cardinality.UNARY_UNARY,
      'ListBooks': cardinality.Cardinality.UNARY_UNARY,
      'UpdateBook': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'server.Library', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)