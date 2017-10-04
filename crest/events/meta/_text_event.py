#
#   _text_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from crest.events.meta._text_meta_event import TextMetaEvent


class TextEvent(TextMetaEvent):
    def __init__(self, text=None, encoding=None):
        if (encoding is None):
            super(TextEvent, self).__init__(text)
        else:
            super(TextEvent, self).__init__(text, encoding)

    def _EventNumber(self):
        return TextEvent.EventNumber()

    @staticmethod
    def EventNumber():
        return 0x01
