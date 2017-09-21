#
#   test_midi_file_writer.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.filing.midi.track import MidiFileData
from crest.filing.midi.track import MidiFileEvent
from crest.filing.midi.track import MidiFileHeader
from crest.filing.midi.track import MidiFileReader
from crest.filing.midi.track import MidiFileWriter

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


class TestMidiFileWriter(unittest.TestCase):
    def test_ctor(self):
        with self.assertRaises(Exception):
            MidiFileWriter(None)

    def test_write(self):
        header = MidiFileHeader(1, 2, 480)
        track1 = []
        track2 = []
        track1.append(MidiFileEvent(0x00, [0x90, 0x40, 0x40]))
        track1.append(MidiFileEvent(0x40, [0x80, 0x40, 0x40]))
        track1.append(MidiFileEvent(0x40, [0xFF, 0x2F, 0x00]))
        track2.append(MidiFileEvent(0x00, [0xFF, 0x2F, 0x00]))
        data = MidiFileData(header, [track1, track2])

        mfw = MidiFileWriter.CreateWithBytesIO()
        mfw.Write(data)
        file_io = mfw.Output
        file_io.seek(0)
        content = file_io.read()
        self.assertEqual(_test, content)


if (__name__ == '__main__'):
    unittest.main()
