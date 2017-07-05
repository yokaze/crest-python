#
#   _midi_chunk_reader.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import io
import struct
from ._midi_chunk import MidiChunk


class MidiChunkReader:
    def __init__(self, input):
        if (input is None):
            raise ValueError('input should be a non-null I/O object.')
        self._input = input

    def ReadChunk(self):
        if self.ReachEnd():
            return None
        else:
            chunkType = self._ReadChunkType()
            chunkLength = self._ReadChunkLength()
            chunkContent = self._input.read(chunkLength)
            return MidiChunk(chunkType, chunkContent)

    def Read(self):
        ret = []
        while (not self.ReachEnd()):
            ret.append(self.ReadChunk())
        return ret if (0 < len(ret)) else None

    def ReachEnd(self):
        offset = self._input.tell()
        self._input.read(1)
        ret = (offset == self._input.tell())
        self._input.seek(offset)
        return ret

    def _ReadChunkType(self):
        return self._input.read(4)

    def _ReadChunkLength(self):
        x = self._input.read(4)
        return struct.unpack('>I', x)[0]

    def _GetInput(self):
        return self._input

    Input = property(_GetInput)

    @staticmethod
    def CreateFromBytes(content):
        return MidiChunkReader(io.BytesIO(content))
