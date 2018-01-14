#
#   _midi_chunk_reader.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import io
import struct

from crest.filing.midi.chunk._midi_chunk import MidiChunk


class MidiChunkReader(object):
    def __init__(self, input):
        if (input is None):
            raise ValueError('input should be a non-null I/O object.')
        self.__input = input

    def ReadChunk(self):
        if self.ReachEnd():
            return None
        else:
            chunkType = self.__ReadChunkType()
            chunkLength = self.__ReadChunkLength()
            chunkContent = self.__input.read(chunkLength)
            return MidiChunk(chunkType, chunkContent)

    def Read(self):
        ret = []
        while (not self.ReachEnd()):
            ret.append(self.ReadChunk())
        return ret if (0 < len(ret)) else None

    def ReachEnd(self):
        offset = self.__input.tell()
        self.__input.read(1)
        ret = (offset == self.__input.tell())
        self.__input.seek(offset)
        return ret

    def __ReadChunkType(self):
        return self.__input.read(4)

    def __ReadChunkLength(self):
        x = self.__input.read(4)
        return struct.unpack('>I', x)[0]

    def __GetInput(self):
        return self.__input

    Input = property(__GetInput)

    @staticmethod
    def CreateFromBytes(content):
        return MidiChunkReader(io.BytesIO(content))
