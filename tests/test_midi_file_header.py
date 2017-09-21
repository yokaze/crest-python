#
#   test_midi_file_header.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.filing.midi.chunk import MidiChunk
from crest.filing.midi.track import MidiFileHeader


class TestMidiFileHeader(unittest.TestCase):
    def test_ctor(self):
        with self.assertRaises(Exception):
            MidiFileHeader(None, None, None)
        with self.assertRaises(Exception):
            MidiFileHeader(-1, 0, 0)
        with self.assertRaises(Exception):
            MidiFileHeader(0, -1, 0)
        with self.assertRaises(Exception):
            MidiFileHeader(0, 0, -1)
        with self.assertRaises(Exception):
            MidiFileHeader(0, 2, 0)

    def test_property(self):
        header = MidiFileHeader(1, 16, 480)
        self.assertEqual(header.Format, 1)
        self.assertEqual(header.TrackCount, 16)
        self.assertEqual(header.Resolution, 480)

    def test_create_chunk(self):
        header = MidiFileHeader(1, 16, 480)
        chunk = header.CreateChunk()
        self.assertTrue(isinstance(chunk, MidiChunk))
        self.assertEqual(chunk.ChunkType, b'MThd')
        self.assertEqual(chunk.Content, b'\0\1\0\x10\1\xE0')

    def test_create_from_bytes(self):
        chunk = b'\0\1\0\x10\1\xE0'
        header = MidiFileHeader.CreateFromBytes(chunk)
        self.assertTrue(isinstance(header, MidiFileHeader))
        self.assertEqual(header.Format, 1)
        self.assertEqual(header.TrackCount, 16)
        self.assertEqual(header.Resolution, 480)


if (__name__ == '__main__'):
    unittest.main()
