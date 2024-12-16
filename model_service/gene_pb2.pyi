from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PredictMutationRequest(_message.Message):
    __slots__ = ("fnaFileData",)
    FNAFILEDATA_FIELD_NUMBER: _ClassVar[int]
    fnaFileData: bytes
    def __init__(self, fnaFileData: _Optional[bytes] = ...) -> None: ...

class PredictMutationReply(_message.Message):
    __slots__ = ("predictions",)
    PREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    predictions: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, predictions: _Optional[_Iterable[float]] = ...) -> None: ...
