#
#   _note_on_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from .primitive._three_bytes_event import ThreeBytesEvent


class NoteOnEvent(ThreeBytesEvent):
    def __init__(self, *args):
        super(NoteOnEvent, self).__init__(*args)

    def _StatusBase(self):
        return 0x90

    def __GetNote(self):
        return self.Parameter1

    def __SetNote(self, note):
        self.Parameter1 = note

    def __GetVelocity(self):
        return self.Parameter2

    def __SetVelocity(self, velocity):
        self.Parameter2 = velocity

    Note = property(__GetNote, __SetNote)
    Velocity = property(__GetVelocity, __SetVelocity)
