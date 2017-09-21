#
#   test_exclusive_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events import ExclusiveEvent


class TestExclusiveEvent(unittest.TestCase):
    def test_message(self):
        evt = ExclusiveEvent([0xF0, 0x01, 0x02, 0x03, 0x04, 0xF7])
        self.assertEqual(evt.Message, [0xF0, 0x01, 0x02, 0x03, 0x04, 0xF7])


if (__name__ == '__main__'):
    unittest.main()
