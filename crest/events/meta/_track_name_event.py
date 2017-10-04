#
#   _track_name_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from crest.events.meta._text_meta_event import TextMetaEvent


class TrackNameEvent(TextMetaEvent):
    def __init__(self, text=None, encoding=None):
        if (encoding is None):
            super(TrackNameEvent, self).__init__(text)
        else:
            super(TrackNameEvent, self).__init__(text, encoding)

    def _EventNumber(self):
        return TrackNameEvent.EventNumber()

    @staticmethod
    def EventNumber():
        return 0x03
