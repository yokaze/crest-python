#
#   test_pitch_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events import PitchEvent


class TestPitchEvent(unittest.TestCase):
    def test_ctor(self):
        PitchEvent()
        PitchEvent(1000)

    def test_message(self):
        evt = PitchEvent()
        self.assertEqual(evt.Message, [0xE0, 0x40, 0])
        evt = PitchEvent(7)
        self.assertEqual(evt.Message, [0xE0, 0x40, 0x07])

    def test_property(self):
        evt = PitchEvent()
        evt.Value = -1000
        self.assertEqual(evt.Parameter1, 0x38)
        self.assertEqual(evt.Parameter2, 0x18)
        self.assertEqual(evt.Value, -1000)


if (__name__ == '__main__'):
    unittest.main()
