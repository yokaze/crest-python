#
#   test_lyric_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events.meta import LyricEvent


class TestLyricEvent(unittest.TestCase):
    def test_ctor(self):
        LyricEvent()
        LyricEvent('Test')
        LyricEvent('Test', 'ascii')

    def test_message(self):
        evt = LyricEvent('Test')
        self.assertEqual(evt.Message, [0xFF, 0x05, 0x04, 0x54, 0x65, 0x73, 0x74])


if (__name__ == '__main__'):
    unittest.main()
