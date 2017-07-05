#
#   _midi_track_writer.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import io
import struct


class MidiTrackWriter:
    def __init__(self, output):
        if (output is None):
            raise ValueError('output should be a non-null I/O object.')
        self._output = output
        self._tick = 0

    def Write(self, events):
        if (events is None):
            return
        for evt in events:
            self.WriteEvent(evt)

    def WriteEvent(self, evt):
        delta = evt.Tick - self._tick
        if (delta < 0):
            raise ValueError('events have been supplied with inverse time order.')
        self._WriteDeltaTime(delta)
        self._WriteMessage(evt.Message)
        self._tick = evt.Tick

    def _WriteDeltaTime(self, delta):
        li = []
        while True:
            li.append(delta & 0x7F)
            delta >>= 7
            if (delta == 0):
                break
        li = li[::-1]
        for i in range(len(li) - 1):
            li[i] |= 0x80

        for b in li:
            self._output.write(struct.pack('>B', b))

    def _WriteMessage(self, msg):
        for b in msg:
            self._output.write(struct.pack('>B', b))

    def _GetOutput(self):
        return self._output

    Output = property(_GetOutput)

    @staticmethod
    def CreateWithBytesIO():
        return MidiTrackWriter(io.BytesIO())
