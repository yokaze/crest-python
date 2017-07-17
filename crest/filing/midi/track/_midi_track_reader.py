#
#   _midi_track_reader.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import io
import struct
import warnings
from ._midi_file_event import MidiFileEvent


class MidiTrackReader(object):
    def __init__(self, input):
        if (input is None):
            raise ValueError('input should be a non-null I/O object.')
        self._input = input
        self._tick = 0
        self._lastStatus = None

    def Read(self):
        ret = []
        while (not self.ReachEnd()):
            ret.append(self.ReadEvent())
        return ret if (0 < len(ret)) else None

    def ReadEvent(self):
        if (self.ReachEnd()):
            return None
        else:
            self._tick += self._ReadDeltaTime()
            return MidiFileEvent(self._tick, self._ReadMessage())

    def ReachEnd(self):
        offset = self._input.tell()
        self._input.read(1)
        ret = (offset == self._input.tell())
        self._input.seek(offset)
        return ret

    def _ReadDeltaTime(self):
        ret = 0
        while True:
            b = self._ReadByte()
            ret = (ret << 7) + (b & 0x7F)
            if ((b & 0x80) == 0):
                break
        return ret

    def _ReadMessage(self):
        MIDI_STATUS_NOTE_OFF = 0x80
        MIDI_STATUS_NOTE_ON = 0x90
        MIDI_STATUS_POLYPHONIC_PRESSURE = 0xA0
        MIDI_STATUS_CONTROL = 0xB0
        MIDI_STATUS_PROGRAM = 0xC0
        MIDI_STATUS_CHANNEL_PRESSURE = 0xD0
        MIDI_STATUS_PITCHBEND = 0xE0
        MIDI_STATUS_SYSTEM = 0xF0
        MIDI_STATUS_EXCLUSIVE_F0 = 0xF0
        MIDI_STATUS_EXCLUSIVE_F7 = 0xF7
        MIDI_STATUS_META = 0xFF

        b = self._ReadByte()
        if (b < 0x80):
            if (self._lastStatus is None):
                raise ValueError('The first MIDI message does not have status byte.')
            msg = [self._lastStatus, b]
        else:
            msg = [b]

        status = msg[0] & 0xF0
        self._lastStatus = status
        if (status in [MIDI_STATUS_PROGRAM,
                       MIDI_STATUS_CHANNEL_PRESSURE]):
            while (len(msg) < 2):
                msg.append(self._ReadByte())
            if (0x80 <= msg[1]):
                warnings.warn('Invalid two-bytes message found: %s' % str(msg), Warning)
                msg[1] = msg[1] if (msg[1] <= 0x7F) else 0x7F
        elif (status in [MIDI_STATUS_NOTE_OFF,
                         MIDI_STATUS_NOTE_ON,
                         MIDI_STATUS_POLYPHONIC_PRESSURE,
                         MIDI_STATUS_CONTROL,
                         MIDI_STATUS_PITCHBEND]):
            while (len(msg) < 3):
                msg.append(self._ReadByte())
            if ((0x80 <= msg[1]) or (0x80 <= msg[2])):
                warnings.warn('Invalid three-bytes message found: %s' % str(msg), Warning)
                msg[1] = msg[1] if (msg[1] <= 0x7F) else 0x7F
                msg[2] = msg[2] if (msg[2] <= 0x7F) else 0x7F
        elif (msg[0] == MIDI_STATUS_META):
            while (len(msg) < 3):
                msg.append(self._ReadByte())
            for i in range(msg[2]):
                msg.append(self._ReadByte())
        elif (msg[0] == MIDI_STATUS_EXCLUSIVE_F0):
            while (len(msg) < 2):
                msg.append(self._ReadByte())
            for i in range(msg[1]):
                msg.append(self._ReadByte())
            if (msg[len(msg) - 1] != 0xF7):
                raise ValueError('F0 message does not end with F7.')
        elif (msg[0] == MIDI_STATUS_EXCLUSIVE_F7):
            while (len(msg) < 2):
                msg.append(self._ReadByte())
            for i in range(msg[1]):
                msg.append(self._ReadByte())
        else:
            raise ValueError('Unknown midi packet found.')

        return msg

    def _ReadByte(self):
        x = self._input.read(1)
        return struct.unpack('>B', x)[0]

    @staticmethod
    def CreateFromBytes(content):
        return MidiTrackReader(io.BytesIO(content))
