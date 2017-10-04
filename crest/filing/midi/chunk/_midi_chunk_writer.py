#
#   _midi_chunk_writer.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import io
import struct

from ._midi_chunk import MidiChunk


class MidiChunkWriter(object):
    def __init__(self, output):
        if (output is None):
            raise ValueError('output should be a non-null I/O object.')
        self.__output = output

    def WriteChunk(self, chunk):
        if (not isinstance(chunk, MidiChunk)):
            raise ValueError('Input should be a MidiChunk.')

        self.__output.write(chunk.ChunkType)
        bChunkLength = struct.pack('>I', len(chunk.Content))
        self.__output.write(bChunkLength)
        self.__output.write(chunk.Content)

    def Write(self, chunks):
        for chunk in chunks:
            self.WriteChunk(chunk)

    def __GetOutput(self):
        return self.__output

    Output = property(__GetOutput)

    @staticmethod
    def CreateWithBytesIO():
        return MidiChunkWriter(io.BytesIO())
