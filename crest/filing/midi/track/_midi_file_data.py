#
#   _midi_file_data.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#


class MidiFileData(object):
    def __init__(self, header, tracks):
        self.__header = header
        self.__tracks = tracks

    def __GetHeader(self):
        return self.__header

    def __GetTracks(self):
        return self.__tracks

    Header = property(__GetHeader)
    Tracks = property(__GetTracks)
