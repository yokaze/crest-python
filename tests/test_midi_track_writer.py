#
#   test_midi_track_writer.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.filing.midi.track import MidiFileEvent
from crest.filing.midi.track import MidiTrackReader, MidiTrackWriter


class TestMidiTrackWriter(unittest.TestCase):
    def test_ctor(self):
        with self.assertRaises(Exception):
            MidiTrackWriter(None)

    def test_write_event(self):
        mtw = MidiTrackWriter.CreateWithBytesIO()
        mtw.WriteEvent(MidiFileEvent(400, [0x90, 0x40, 0x40]))
        track_io = mtw.Output
        track_io.seek(0)

        mtr = MidiTrackReader(track_io)
        evt = mtr.ReadEvent()
        self.assertEqual(evt.Tick, 400)
        self.assertEqual(evt.Message, [0x90, 0x40, 0x40])

    def test_write(self):
        mtw = MidiTrackWriter.CreateWithBytesIO()
        mtw.Write(None)
        evt1 = MidiFileEvent(400, [0x90, 0x40, 0x40])
        evt2 = MidiFileEvent(600, [0x80, 0x40, 0x40])
        mtw.Write([evt1, evt2])
        track_io = mtw.Output
        track_io.seek(0)

        mtr = MidiTrackReader(track_io)
        events = mtr.Read()
        self.assertEqual(events[0].Tick, 400)
        self.assertEqual(events[0].Message, [0x90, 0x40, 0x40])
        self.assertEqual(events[1].Tick, 600)
        self.assertEqual(events[1].Message, [0x80, 0x40, 0x40])

    def test_raise(self):
        mtw = MidiTrackWriter.CreateWithBytesIO()
        mtw.WriteEvent(MidiFileEvent(400, [0x90, 0x40, 0x40]))
        with self.assertRaises(Exception):
            mtw.WriteEvent(MidiFileEvent(200, [0x90, 0x40, 0x40]))


if (__name__ == '__main__'):
    unittest.main()
