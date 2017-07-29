#
#   _copyright_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from ._text_meta_event import TextMetaEvent


class CopyrightEvent(TextMetaEvent):
    def __init__(self, text=None, encoding=None):
        if (encoding is None):
            super(CopyrightEvent, self).__init__(text)
        else:
            super(CopyrightEvent, self).__init__(text, encoding)

    def _EventNumber(self):
        return CopyrightEvent.EventNumber()

    @staticmethod
    def EventNumber():
        return 0x02
