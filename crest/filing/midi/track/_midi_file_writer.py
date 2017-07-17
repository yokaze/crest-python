#
#   _midi_file_writer.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import io
from ..chunk._midi_chunk import MidiChunk
from ..chunk._midi_chunk_writer import MidiChunkWriter
from ._midi_file_data import MidiFileData
from ._midi_track_writer import MidiTrackWriter


class MidiFileWriter(object):
    def __init__(self, output):
        self._output = output
        self._mcw = MidiChunkWriter(output)

    def Write(self, fileData):
        if (not isinstance(fileData, MidiFileData)):
            raise ValueError('Argument should be a MidiFileData.')

        self._mcw.WriteChunk(fileData.Header.CreateChunk())
        for track in fileData.Tracks:
            buffer = io.BytesIO()
            mtw = MidiTrackWriter(buffer)
            mtw.Write(track)
            buffer.seek(0)
            self._mcw.WriteChunk(MidiChunk(b'MTrk', buffer.read()))

    def _GetOutput(self):
        return self._output

    Output = property(_GetOutput)

    @staticmethod
    def CreateWithBytesIO():
        return MidiFileWriter(io.BytesIO())
