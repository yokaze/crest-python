#
#   _control_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from crest.events.primitive._three_bytes_event import ThreeBytesEvent


class ControlEvent(ThreeBytesEvent):
    def __init__(self, *args):
        super(ControlEvent, self).__init__(*args)

    def _StatusBase(self):
        return 0xB0

    def __GetNumber(self):
        return self.Parameter1

    def __SetNumber(self, number):
        self.Parameter1 = number

    def __GetValue(self):
        return self.Parameter2

    def __SetValue(self, value):
        self.Parameter2 = value

    Number = property(__GetNumber, __SetNumber)
    Value = property(__GetValue, __SetValue)
