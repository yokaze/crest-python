#
#   test_marker_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events.meta import MarkerEvent


class TestMarkerEvent(unittest.TestCase):
    def test_ctor(self):
        MarkerEvent()
        MarkerEvent('Test')
        MarkerEvent('Test', 'ascii')

    def test_message(self):
        evt = MarkerEvent('Test')
        self.assertEqual(evt.Message, [0xFF, 0x06, 0x04, 0x54, 0x65, 0x73, 0x74])


if (__name__ == '__main__'):
    unittest.main()
