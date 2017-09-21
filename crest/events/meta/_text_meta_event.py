#
#   _text_meta_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from ._meta_event import MetaEvent
import array
import codecs
import platform


class TextMetaEvent(MetaEvent):
    def __init__(self, text=None, encoding='ascii'):
        super(TextMetaEvent, self).__init__()
        self.__SetText(text)
        self.__SetEncoding(encoding)

    def _EventContent(self):
        arr = array.array('B')
        if (platform.python_version_tuple()[0] == '2'):
            arr.fromstring(codecs.encode(self.__text, self.__encoding))
        else:
            arr.frombytes(codecs.encode(self.__text, self.__encoding))

        return arr.tolist()

    def __GetText(self):
        return self.__text

    def __SetText(self, text):
        self.__text = str(text)

    def __GetEncoding(self):
        return self.__encoding

    def __SetEncoding(self, encoding):
        self.__encoding = str(encoding)

    Text = property(__GetText, __SetText)
    Encoding = property(__GetEncoding, __SetEncoding)
