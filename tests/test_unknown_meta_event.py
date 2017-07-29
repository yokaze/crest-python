#
#   test_unknown_meta_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events.meta import UnknownMetaEvent


class TestUnknownMetaEvent(unittest.TestCase):
    def test_ctor(self):
        with self.assertRaises(Exception):
            UnknownMetaEvent()
        UnknownMetaEvent(1)
        UnknownMetaEvent(1, [0x01, 0x02, 0x03])

    def test_message(self):
        evt = UnknownMetaEvent(1)
        self.assertEqual(evt.Message, [0xFF, 0x01, 0x00])
        evt = UnknownMetaEvent(1, [0x01, 0x02, 0x03])
        self.assertEqual(evt.Message, [0xFF, 0x01, 0x03, 0x01, 0x02, 0x03])

if (__name__ == '__main__'):
    unittest.main()
