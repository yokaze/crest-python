#
#   test_time_signature_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events.meta import TimeSignatureEvent


class TestTimeSignatureEvent(unittest.TestCase):
    def test_ctor(self):
        TimeSignatureEvent()
        TimeSignatureEvent(3)
        TimeSignatureEvent(4, 4)
        with self.assertRaises(Exception):
            TimeSignatureEvent(2, 3)

    def test_message(self):
        evt = TimeSignatureEvent(5, 8)
        self.assertEqual(evt.Message, [0xFF, 0x58, 0x04, 0x05, 0x03, 0x18, 0x08])

    def test_property(self):
        evt = TimeSignatureEvent()
        evt.Beat = 5
        evt.Note = 8
        self.assertEqual(evt.Beat, 5)
        self.assertEqual(evt.Note, 8)
        with self.assertRaises(Exception):
            evt.Note = 7


if (__name__ == '__main__'):
    unittest.main()
