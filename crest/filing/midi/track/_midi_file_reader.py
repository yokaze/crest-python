#
#   _midi_file_reader.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import io

from crest.filing.midi.chunk._midi_chunk_reader import MidiChunkReader
from crest.filing.midi.track._midi_file_data import MidiFileData
from crest.filing.midi.track._midi_file_header import MidiFileHeader
from crest.filing.midi.track._midi_track_reader import MidiTrackReader


class MidiFileReader(object):
    def __init__(self, input):
        if (input is None):
            raise ValueError('input should be a non-null I/O object.')
        self.__input = input

    def Read(self):
        mcr = MidiChunkReader(self.__input)
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
