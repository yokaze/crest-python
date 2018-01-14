#
#   _midi_file_writer.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import io

from crest.filing.midi.chunk._midi_chunk import MidiChunk
from crest.filing.midi.chunk._midi_chunk_writer import MidiChunkWriter
from crest.filing.midi.track._midi_file_data import MidiFileData
from crest.filing.midi.track._midi_track_writer import MidiTrackWriter


class MidiFileWriter(object):
    def __init__(self, output):
        self.__output = output
        self.__mcw = MidiChunkWriter(output)

    def Write(self, fileData):
        if (not isinstance(fileData, MidiFileData)):
            raise ValueError('Argument should be a MidiFileData.')

        self.__mcw.WriteChunk(fileData.Header.CreateChunk())
        for track in fileData.Tracks:
            buffer = io.BytesIO()
            mtw = MidiTrackWriter(buffer)
            mtw.Write(track)
            buffer.seek(0)
            self.__mcw.WriteChunk(MidiChunk(b'MTrk', buffer.read()))

    def __GetOutput(self):
        return self.__output

    Output = property(__GetOutput)

    @staticmethod
    def CreateWithBytesIO():
        return MidiFileWriter(io.BytesIO())
