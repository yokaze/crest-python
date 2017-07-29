#
#   _midi_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from ._abstract_midi_event import AbstractMidiEvent
import abc


class MidiEvent(AbstractMidiEvent):
    def __init__(self):
        super(MidiEvent, self).__init__()
        self.__channel = 0
        self.__tick = 0

    def _GetChannel(self):
        return self.__channel

    def _SetChannel(self, channel):
        channel = int(channel)
        if ((channel < 0) or (16 <= channel)):
            raise ValueError('channel should be from 0 to 15.')
        self.__channel = int(channel)

    def _GetTick(self):
        return self.__tick

    def _SetTick(self, tick):
        self.__tick = int(tick)
