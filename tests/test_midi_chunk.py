#
#   test_midi_chunk.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.filing.midi.chunk import MidiChunk


class TestMidiChunk(unittest.TestCase):
    def test_ctor(self):
        MidiChunk(b'MThd', b'\0\0\0\0\0\0')
        MidiChunk(b'MTrk', b'')
        with self.assertRaises(Exception):
            MidiChunk(b'MThd', None)
        with self.assertRaises(Exception):
            MidiChunk(b'MThd', b'')
        with self.assertRaises(Exception):
            MidiChunk(b'MTrk', None)
        with self.assertRaises(Exception):
            MidiChunk(b'', b'')

    def test_get_chunk_type(self):
        chunk = MidiChunk(b'MThd', b'\0\0\0\0\0\0')
        self.assertEqual(chunk.ChunkType, b'MThd')

        chunk = MidiChunk(b'MTrk', b'')
        self.assertEqual(chunk.ChunkType, b'MTrk')

    def test_get_content(self):
        chunk = MidiChunk(b'MTrk', b'1234')
        self.assertEqual(chunk.Content, b'1234')


if (__name__ == '__main__'):
    unittest.main()
