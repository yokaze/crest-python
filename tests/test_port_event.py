#
#   test_port_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events.meta import PortEvent


class TestPortEvent(unittest.TestCase):
    def test_ctor(self):
        PortEvent()
        PortEvent(4)

    def test_message(self):
        evt = PortEvent(4)
        self.assertEqual(evt.Message, [0xFF, 0x21, 0x01, 0x04])

if (__name__ == '__main__'):
    unittest.main()
