#
#   _channel_pressure_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from crest.events.primitive._two_bytes_event import TwoBytesEvent


class ChannelPressureEvent(TwoBytesEvent):
    def __init__(self, *args):
        super(ChannelPressureEvent, self).__init__(*args)

    def _StatusBase(self):
        return 0xD0

    def __GetValue(self):
        return self.Parameter

    def __SetValue(self, value):
        self.Parameter = value

    Value = property(__GetValue, __SetValue)
