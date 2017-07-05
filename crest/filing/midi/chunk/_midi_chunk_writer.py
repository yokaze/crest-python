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


class MidiChunkWriter:
    def __init__(self, output):
        if (output is None):
            raise ValueError('output should be a non-null I/O object.')
        self._output = output

    def WriteChunk(self, chunk):
        if (not isinstance(chunk, MidiChunk)):
            raise ValueError('Input should be a MidiChunk.')

        self._output.write(chunk.ChunkType)
        bChunkLength = struct.pack('>I', len(chunk.Content))
        self._output.write(bChunkLength)
        self._output.write(chunk.Content)

    def Write(self, chunks):
        for chunk in chunks:
            self.WriteChunk(chunk)

    def _GetOutput(self):
        return self._output

    Output = property(_GetOutput)

    @staticmethod
    def CreateWithBytesIO():
        return MidiChunkWriter(io.BytesIO())
