#
#   _pitch_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from crest.events.primitive._three_bytes_event import ThreeBytesEvent


class PitchEvent(ThreeBytesEvent):
    def __init__(self, value=0):
        super(PitchEvent, self).__init__()
        self.__SetValue(value)

    def _StatusBase(self):
        return 0xE0

    def __GetValue(self):
        return (self.Parameter1 << 7) + self.Parameter2 - 0x2000

    def __SetValue(self, value):
        value += 0x2000
        self.Parameter1 = value >> 7
        self.Parameter2 = value & 0x7F

    Value = property(__GetValue, __SetValue)
