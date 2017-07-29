#
#   test_control_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events import ControlEvent


class TestControlEvent(unittest.TestCase):
    def test_ctor(self):
        ControlEvent()
        ControlEvent(10)
        ControlEvent(10, 20)

    def test_message(self):
        evt = ControlEvent()
        self.assertEqual(evt.Message, [0xB0, 0, 0])
        evt = ControlEvent(7)
        self.assertEqual(evt.Message, [0xB0, 7, 0])
        evt = ControlEvent(3, 7)
        self.assertEqual(evt.Message, [0xB0, 3, 7])

    def test_property(self):
        evt = ControlEvent()
        evt.Number = 7
        evt.Value = 15
        self.assertEqual(evt.Parameter1, 7)
        self.assertEqual(evt.Parameter2, 15)

if (__name__ == '__main__'):
    unittest.main()
