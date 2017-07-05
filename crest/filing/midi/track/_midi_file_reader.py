#
#   _midi_file_reader.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import io
from .. import chunk
from ._midi_file_data import MidiFileData
from ._midi_file_header import MidiFileHeader
from ._midi_track_reader import MidiTrackReader


class MidiFileReader:
    def __init__(self, input):
        if (input is None):
            raise ValueError('input should be a non-null I/O object.')
        self._input = input

    def Read(self):
        mcr = chunk.MidiChunkReader(self._input)
        chunks = mcr.Read()
        if (chunks is None):
            return None

        headerChunk = chunks[0]
        fileHeader = MidiFileHeader.CreateFromBytes(headerChunk.Content)

        trackChunks = chunks[1:]
        tracks = []
        for trackChunk in trackChunks:
            mtr = MidiTrackReader.CreateFromBytes(trackChunk.Content)
            tracks.append(mtr.Read())

        return MidiFileData(fileHeader, tracks)

    @staticmethod
    def CreateFromBytes(content):
        return MidiFileReader(io.BytesIO(content))
