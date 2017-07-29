#
#   test_midi_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events import MidiEvent
from crest.events import ProgramEvent


class TestMidiEvent(unittest.TestCase):
    def test_ctor(self):
        MidiEvent()

    def test_channel(self):
        evt = MidiEvent()
        self.assertEqual(evt.Channel, 0)
        with self.assertRaises(Exception):
            evt.Channel = -1
        with self.assertRaises(Exception):
            evt.Channel = 16
        evt.Channel = 1.
        self.assertTrue(type(evt.Channel) == int)
        self.assertEqual(evt.Channel, 1)

    def test_tick(self):
        evt = MidiEvent()
        self.assertEqual(evt.Tick, 0)
        evt.Tick = 2.
        self.assertTrue(type(evt.Tick) == int)
        self.assertEqual(evt.Tick, 2)

    def test_message(self):
        evt = MidiEvent()
        self.assertEqual(evt.Message, None)

if (__name__ == '__main__'):
    unittest.main()
