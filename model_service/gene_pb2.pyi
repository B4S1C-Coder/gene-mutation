from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class predictLabelRequest(_message.Message):
    __slots__ = ("fileData",)
    FILEDATA_FIELD_NUMBER: _ClassVar[int]
    fileData: bytes
    def __init__(self, fileData: _Optional[bytes] = ...) -> None: ...

class predictLabelReply(_message.Message):
    __slots__ = ("predictedLabel",)
    PREDICTEDLABEL_FIELD_NUMBER: _ClassVar[int]
    predictedLabel: str
    def __init__(self, predictedLabel: _Optional[str] = ...) -> None: ...
