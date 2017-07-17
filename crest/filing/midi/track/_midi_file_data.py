#
#   _midi_file_data.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#


class MidiFileData(object):
    def __init__(self, header, tracks):
        self._header = header
        self._tracks = tracks

    def _GetHeader(self):
        return self._header

    def _GetTracks(self):
        return self._tracks

    Header = property(_GetHeader)
    Tracks = property(_GetTracks)
