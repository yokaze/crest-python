#
#   _program_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from crest.events.primitive._two_bytes_event import TwoBytesEvent


class ProgramEvent(TwoBytesEvent):
    def __init__(self, parameter=0):
        super(ProgramEvent, self).__init__(parameter)

    def _StatusBase(self):
        return 0xC0

    def __GetValue(self):
        return self.Parameter

    def __SetValue(self, value):
        self.Parameter = value

    Value = property(__GetValue, __SetValue)
