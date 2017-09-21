#
#   test_midi_file_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.filing.midi.track import MidiFileEvent


class TestMidiFileEvent(unittest.TestCase):
    def test(self):
        evt = MidiFileEvent(100, [1, 2, 3, 4])
        self.assertEqual(evt.Tick, 100)
        self.assertEqual(evt.Message, [1, 2, 3, 4])


if (__name__ == '__main__'):
    unittest.main()
