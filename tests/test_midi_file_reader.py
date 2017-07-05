#
#   test_midi_file_reader.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import io
import struct
import unittest
from crest.filing.midi.track import MidiFileData
from crest.filing.midi.track import MidiFileHeader
from crest.filing.midi.track import MidiFileReader

_test = b'\x4D\x54\x68\x64' + \
        b'\x00\x00\x00\x06' + \
        b'\x00\x01\x00\x02\x01\xE0' + \
        b'\x4D\x54\x72\x6B' + \
        b'\x00\x00\x00\x0C' + \
        b'\x00\x90\x40\x40' + \
        b'\x40\x80\x40\x40' + \
        b'\x00\xFF\x2F\x00' + \
        b'\x4D\x54\x72\x6B' + \
        b'\x00\x00\x00\x04' + \
        b'\x00\xFF\x2F\x00'


class TestMidiFileReader(unittest.TestCase):
    def test_ctor(self):
        with self.assertRaises(Exception):
            MidiFileReader(None)

    def test_read(self):
        mfr = MidiFileReader.CreateFromBytes(_test)
        data = mfr.Read()
        self.assertTrue(isinstance(data, MidiFileData))
        self.assertTrue(isinstance(data.Header, MidiFileHeader))
        self.assertEqual(data.Header.Format, 1)
        self.assertEqual(data.Header.TrackCount, 2)
        self.assertEqual(data.Header.Resolution, 480)
        self.assertEqual(len(data.Tracks), 2)

if (__name__ == '__main__'):
    unittest.main()
