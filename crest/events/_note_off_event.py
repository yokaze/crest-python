#
#   _note_off_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from .primitive._three_bytes_event import ThreeBytesEvent


class NoteOffEvent(ThreeBytesEvent):
    def __init__(self, *args):
        super(NoteOffEvent, self).__init__(*args)

    def _StatusBase(self):
        return 0x80

    def __GetNote(self):
        return self.Parameter1

    def __SetNote(self, note):
        self.Parameter1 = note

    def __GetNoteOffVelocity(self):
        return self.Parameter2

    def __SetNoteOffVelocity(self, noteOffVelocity):
        self.Parameter2 = noteOffVelocity

    Note = property(__GetNote, __SetNote)
    NoteOffVelocity = property(__GetNoteOffVelocity, __SetNoteOffVelocity)
