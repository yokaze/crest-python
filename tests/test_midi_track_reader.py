#
#   test_midi_track_reader.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.filing.midi.track import MidiFileEvent, MidiTrackReader


class TestMidiTrackReader(unittest.TestCase):
    def test_ctor(self):
        with self.assertRaises(Exception):
            MidiTrackReader(None)

    def test_read(self):
        content = b''
        mtr = MidiTrackReader.CreateFromBytes(content)
        events = mtr.Read()
        self.assertEqual(events, None)

    def test_note_on(self):
        content = b'\0\x90\x40\x40'
        mtr = MidiTrackReader.CreateFromBytes(content)
        evt = mtr.ReadEvent()
        self.assertTrue(isinstance(evt, MidiFileEvent))
        self.assertEqual(evt.Tick, 0)
        self.assertEqual(evt.Message, [0x90, 0x40, 0x40])

    def test_note_off(self):
        content = b'\0\x80\x40\x40'
        mtr = MidiTrackReader.CreateFromBytes(content)
        evt = mtr.ReadEvent()
        self.assertTrue(isinstance(evt, MidiFileEvent))
        self.assertEqual(evt.Tick, 0)
        self.assertEqual(evt.Message, [0x80, 0x40, 0x40])

    def test_cc(self):
        content = b'\0\xB0\x40\x7F'
        mtr = MidiTrackReader.CreateFromBytes(content)
        evt = mtr.ReadEvent()
        self.assertTrue(isinstance(evt, MidiFileEvent))
        self.assertEqual(evt.Tick, 0)
        self.assertEqual(evt.Message, [0xB0, 0x40, 0x7F])

    def test_program(self):
        content = b'\0\xC0\x40'
        mtr = MidiTrackReader.CreateFromBytes(content)
        evt = mtr.ReadEvent()
        self.assertTrue(isinstance(evt, MidiFileEvent))
        self.assertEqual(evt.Tick, 0)
        self.assertEqual(evt.Message, [0xC0, 0x40])

    def test_pitch(self):
        content = b'\0\xE0\x40\x40'
        mtr = MidiTrackReader.CreateFromBytes(content)
        evt = mtr.ReadEvent()
        self.assertTrue(isinstance(evt, MidiFileEvent))
        self.assertEqual(evt.Tick, 0)
        self.assertEqual(evt.Message, [0xE0, 0x40, 0x40])

    def test_exclusive_f0(self):
        content = b'\0\xF0\4\0\1\2\xF7'
        mtr = MidiTrackReader.CreateFromBytes(content)
        evt = mtr.ReadEvent()
        self.assertTrue(isinstance(evt, MidiFileEvent))
        self.assertEqual(evt.Tick, 0)
        self.assertEqual(evt.Message, [0xF0, 4, 0, 1, 2, 0xF7])

    def test_exclusive_f7(self):
        content = b'\0\xF7\4\0\1\2\3'
        mtr = MidiTrackReader.CreateFromBytes(content)
        evt = mtr.ReadEvent()
        self.assertTrue(isinstance(evt, MidiFileEvent))
        self.assertEqual(evt.Tick, 0)
        self.assertEqual(evt.Message, [0xF7, 4, 0, 1, 2, 3])

    def test_meta(self):
        content = b'\0\xFF\1\4Test\x40\xFF\1\4Meta'
        msg1 = [0xFF, 0x1, 0x4, ord('T'), ord('e'), ord('s'), ord('t')]
        msg2 = [0xFF, 0x1, 0x4, ord('M'), ord('e'), ord('t'), ord('a')]

        mtr = MidiTrackReader.CreateFromBytes(content)
        events = mtr.Read()
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0].Tick, 0)
        self.assertEqual(events[0].Message, msg1)
        self.assertEqual(events[1].Tick, 0x40)
        self.assertEqual(events[1].Message, msg2)

    def test_running_status(self):
        content = b'\0\x90\x40\x40\0\x60\x40\0\xB0\x0A\x7F\0\x0A\x40'
        mtr = MidiTrackReader.CreateFromBytes(content)
        events = mtr.Read()
        self.assertEqual(len(events), 4)
        self.assertEqual(events[0].Tick, 0)
        self.assertEqual(events[0].Message, [0x90, 0x40, 0x40])
        self.assertEqual(events[1].Tick, 0)
        self.assertEqual(events[1].Message, [0x90, 0x60, 0x40])
        self.assertEqual(events[2].Tick, 0)
        self.assertEqual(events[2].Message, [0xB0, 0x0A, 0x7F])
        self.assertEqual(events[3].Tick, 0)
        self.assertEqual(events[3].Message, [0xB0, 0x0A, 0x40])

    def test_delta_tick(self):
        content = b'\0\x90\x40\x40\x81\x81\0\x80\x40\x40'
        mtr = MidiTrackReader.CreateFromBytes(content)
        events = mtr.Read()
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0].Tick, 0)
        self.assertEqual(events[0].Message, [0x90, 0x40, 0x40])
        self.assertEqual(events[1].Tick, (1 << 14) + (1 << 7))
        self.assertEqual(events[1].Message, [0x80, 0x40, 0x40])

if (__name__ == '__main__'):
    unittest.main()
