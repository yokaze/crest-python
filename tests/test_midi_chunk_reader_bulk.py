#
#   test_midi_chunk_reader_bulk.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import os
import unittest
from crest.filing.midi.chunk import MidiChunkReader


class TestMidiChunkReaderBulk(unittest.TestCase):
    def test_read(self):
        midi_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'midi'))
        for fname in os.listdir(midi_dir):
            body, ext = os.path.splitext(fname)
            if ((ext.lower() == '.mid') or (ext.lower() == '.midi')):
                fpath = os.path.join(midi_dir, fname)
                with open(fpath, 'rb') as fp:
                    mcr = MidiChunkReader(fp)
                    mcr.Read()


if (__name__ == '__main__'):
    unittest.main()
