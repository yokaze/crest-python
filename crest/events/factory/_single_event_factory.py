#
#   _single_event_factory.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from crest.events._channel_pressure_event import ChannelPressureEvent
from crest.events._control_event import ControlEvent
from crest.events._exclusive_event import ExclusiveEvent
from crest.events._key_pressure_event import KeyPressureEvent
from crest.events._note_off_event import NoteOffEvent
from crest.events._note_on_event import NoteOnEvent
from crest.events._pitch_event import PitchEvent
from crest.events._program_event import ProgramEvent
from crest.events.factory._abstract_event_factory import AbstractEventFactory
from crest.events.factory._convert_result import ConvertResult
from crest.events.factory._meta_event_factory import MetaEventFactory


class SingleEventFactory(AbstractEventFactory):
    def __init__(self):
        super(SingleEventFactory, self).__init__()
        self._metaFactory = MetaEventFactory()

    def Input(self, tick, message):
        MIDI_STATUS_NOTE_OFF = 0x80
        MIDI_STATUS_NOTE_ON = 0x90
        MIDI_STATUS_POLYPHONIC_PRESSURE = 0xA0
        MIDI_STATUS_CONTROL = 0xB0
        MIDI_STATUS_PROGRAM = 0xC0
        MIDI_STATUS_CHANNEL_PRESSURE = 0xD0
        MIDI_STATUS_PITCHBEND = 0xE0
        MIDI_STATUS_EXCLUSIVE = 0xF0
        MIDI_STATUS_META = 0xFF

        if (message[0] == MIDI_STATUS_META):
            return self._metaFactory.Input(tick, message)
        elif (message[0] == MIDI_STATUS_EXCLUSIVE):
            evt = ExclusiveEvent(message)
            evt.Tick = tick
            return ConvertResult(True, evt)

        status_upper = message[0] & 0xF0
        if (status_upper == MIDI_STATUS_NOTE_OFF):
            evt = NoteOffEvent(message[1], message[2])
        elif (status_upper == MIDI_STATUS_NOTE_ON):
            if (message[2] == 0):
                evt = NoteOffEvent(message[1])
            else:
                evt = NoteOnEvent(message[1], message[2])
        elif (status_upper == MIDI_STATUS_POLYPHONIC_PRESSURE):
            evt = KeyPressureEvent(message[1], message[2])
        elif (status_upper == MIDI_STATUS_CONTROL):
            evt = ControlEvent(message[1], message[2])
        elif (status_upper == MIDI_STATUS_PROGRAM):
            evt = ProgramEvent(message[1])
        elif (status_upper == MIDI_STATUS_CHANNEL_PRESSURE):
            evt = ChannelPressureEvent(message[1])
        elif (status_upper == MIDI_STATUS_PITCHBEND):
            evt = PitchEvent((message[1] << 7) + message[2] - 0x2000)
        else:
            assert False

        evt.Tick = tick
        return ConvertResult(True, evt)

    def Finalize(self):
        return ConvertResult(False)
