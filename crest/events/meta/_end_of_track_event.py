#
#   _end_of_track_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from ._meta_event import MetaEvent


class EndOfTrackEvent(MetaEvent):
    def __init__(self):
        super(EndOfTrackEvent, self).__init__()

    def _EventNumber(self):
        return EndOfTrackEvent.EventNumber()

    def _EventContent(self):
        return None

    @staticmethod
    def EventNumber():
        return 0x2F
