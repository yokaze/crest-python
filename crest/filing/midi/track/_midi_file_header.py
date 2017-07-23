#
#   _midi_file_header.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import struct
from ..chunk._midi_chunk import MidiChunk


class MidiFileHeader(object):
    def __init__(self, format, trackCount, resolution):
        if ((format < 0) or (3 <= format)):
            raise ValueError('format should be zero, one or two.')
        if ((format == 0) and (trackCount != 1)):
            raise ValueError('If format is one, trackCound should also be one.')
        if (trackCount < 0):
            raise ValueError('trackCound should be positive.')
        if (resolution < 0):
            raise ValueError('resolution should be positive.')
        self.__format = int(format)
        self.__trackCount = int(trackCount)
        self.__resolution = int(resolution)

    def CreateChunk(self):
        content = struct.pack('>HHH',
                              self.__format,
                              self.__trackCount,
                              self.__resolution)

        return MidiChunk(b'MThd', content)

    def __GetFormat(self):
        return self.__format

    def __GetTrackCount(self):
        return self.__trackCount

    def __GetResolution(self):
        return self.__resolution

    Format = property(__GetFormat)
    TrackCount = property(__GetTrackCount)
    Resolution = property(__GetResolution)

    @staticmethod
    def CreateFromBytes(content):
        format, trackCount, resolution = struct.unpack('>HHH', content)
        return MidiFileHeader(format, trackCount, resolution)
