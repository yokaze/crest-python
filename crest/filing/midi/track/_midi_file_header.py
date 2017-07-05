#
#   _midi_file_header.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import struct
from .. import chunk


class MidiFileHeader:
    def __init__(self, format, trackCount, resolution):
        if ((format < 0) or (3 <= format)):
            raise ValueError('format should be zero, one or two.')
        if ((format == 0) and (trackCount != 1)):
            raise ValueError('If format is one, trackCound should also be one.')
        if (trackCount < 0):
            raise ValueError('trackCound should be positive.')
        if (resolution < 0):
            raise ValueError('resolution should be positive.')
        self._format = int(format)
        self._trackCount = int(trackCount)
        self._resolution = int(resolution)

    def CreateChunk(self):
        content = struct.pack('>HHH',
                              self._format,
                              self._trackCount,
                              self._resolution)

        return chunk.MidiChunk(b'MThd', content)

    def _GetFormat(self):
        return self._format

    def _GetTrackCount(self):
        return self._trackCount

    def _GetResolution(self):
        return self._resolution

    Format = property(_GetFormat)
    TrackCount = property(_GetTrackCount)
    Resolution = property(_GetResolution)

    @staticmethod
    def CreateFromBytes(content):
        format, trackCount, resolution = struct.unpack('>HHH', content)
        return MidiFileHeader(format, trackCount, resolution)
