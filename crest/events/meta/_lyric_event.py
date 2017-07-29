#
#   _lyric_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from ._text_meta_event import TextMetaEvent


class LyricEvent(TextMetaEvent):
    def __init__(self, text=None, encoding=None):
        if (encoding is None):
            super(LyricEvent, self).__init__(text)
        else:
            super(LyricEvent, self).__init__(text, encoding)

    def _EventNumber(self):
        return LyricEvent.EventNumber()

    @staticmethod
    def EventNumber():
        return 0x05
