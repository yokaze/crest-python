#
#   _midi_track_writer.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import io
import struct


class MidiTrackWriter(object):
    def __init__(self, output):
        if (output is None):
            raise ValueError('output should be a non-null I/O object.')
        self.__output = output
        self.__tick = 0

    def Write(self, events):
        if (events is None):
            return
        for evt in events:
            self.WriteEvent(evt)

    def WriteEvent(self, evt):
        delta = evt.Tick - self.__tick
        if (delta < 0):
            raise ValueError('events have been supplied with inverse time order.')
        self.__WriteDeltaTime(delta)
        self.__WriteMessage(evt.Message)
        self.__tick = evt.Tick

    def __WriteDeltaTime(self, delta):
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
            self.__output.write(struct.pack('>B', b))

    def __WriteMessage(self, msg):
        for b in msg:
            self.__output.write(struct.pack('>B', b))

    def __GetOutput(self):
        return self.__output

    Output = property(__GetOutput)

    @staticmethod
    def CreateWithBytesIO():
        return MidiTrackWriter(io.BytesIO())
