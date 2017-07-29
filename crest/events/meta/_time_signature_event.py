#
#   _time_signature_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import math
from ._meta_event import MetaEvent


class TimeSignatureEvent(MetaEvent):
    def __init__(self, beat=4, note=4):
        super(TimeSignatureEvent, self).__init__()
        self.__SetBeat(beat)
        self.__SetNote(note)

    def _EventNumber(self):
        return TimeSignatureEvent.EventNumber()

    def _EventContent(self):
        note_expression = int(round(math.log(self.__note, 2)))
        return [self.__beat, note_expression, 0x18, 0x08]

    def __GetBeat(self):
        return self.__beat

    def __SetBeat(self, beat):
        self.__beat = int(beat)

    def __GetNote(self):
        return self.__note

    def __SetNote(self, note):
        note = int(note)
        if (note in [1, 2, 4, 8, 16, 32, 64, 128, 256]):
            self.__note = note
        else:
            raise ValueError('Note should be a power of two.')

    Beat = property(__GetBeat, __SetBeat)
    Note = property(__GetNote, __SetNote)

    @staticmethod
    def EventNumber():
        return 0x58
