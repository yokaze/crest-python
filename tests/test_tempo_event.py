#
#   test_tempo_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events.meta import TempoEvent


class TestTempoEvent(unittest.TestCase):
    def test_ctor(self):
        TempoEvent()
        TempoEvent(120)

    def test_message(self):
        evt = TempoEvent(120)
        self.assertEqual(evt.Message, [0xFF, 0x51, 0x03, 0x07, 0xA1, 0x20])

    def test_property(self):
        evt = TempoEvent(120)
        self.assertEqual(evt.Tempo, 120)
        self.assertEqual(evt.MicroSeconds, 500000)
        evt.Tempo = 60
        self.assertEqual(evt.Tempo, 60)
        self.assertEqual(evt.MicroSeconds, 1000000)
        evt.MicroSeconds = 250000
        self.assertEqual(evt.Tempo, 240)
        self.assertEqual(evt.MicroSeconds, 250000)

if (__name__ == '__main__'):
    unittest.main()
