#
#   _key_pressure_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from crest.events.primitive._three_bytes_event import ThreeBytesEvent


class KeyPressureEvent(ThreeBytesEvent):
    def __init__(self, *args):
        super(KeyPressureEvent, self).__init__(*args)

    def _StatusBase(self):
        return 0xA0

    def __GetNote(self):
        return self.Parameter1

    def __SetNote(self, number):
        self.Parameter1 = number

    def __GetValue(self):
        return self.Parameter2

    def __SetValue(self, value):
        self.Parameter2 = value

    Note = property(__GetNote, __SetNote)
    Value = property(__GetValue, __SetValue)
