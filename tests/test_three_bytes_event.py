#
#   test_two_bytes_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events import ControlEvent


class TestThreeBytesEvent(unittest.TestCase):
    def test_ctor(self):
        ControlEvent()
        ControlEvent(1)
        ControlEvent(1, 2)
        evt = ControlEvent(1., 2.)
        self.assertTrue(type(evt.Parameter1) == int)
        self.assertTrue(type(evt.Parameter2) == int)
        self.assertEqual(evt.Parameter1, 1)
        self.assertEqual(evt.Parameter2, 2)

        with self.assertRaises(Exception):
            ControlEvent(None)
        with self.assertRaises(Exception):
            ControlEvent(-1)
        with self.assertRaises(Exception):
            ControlEvent(128)
        with self.assertRaises(Exception):
            ControlEvent(0, -1)
        with self.assertRaises(Exception):
            ControlEvent(0, 128)
        with self.assertRaises(Exception):
            ControlEvent(0, 0, 0)

    def test_parameters(self):
        evt = ControlEvent()
        evt.Parameter1 = 1.
        evt.Parameter2 = 2.
        self.assertTrue(type(evt.Parameter1) == int)
        self.assertTrue(type(evt.Parameter2) == int)
        self.assertEqual(evt.Parameter1, 1)
        self.assertEqual(evt.Parameter2, 2)

        with self.assertRaises(Exception):
            evt.Parameter1 = None
        with self.assertRaises(Exception):
            evt.Parameter1 = -1
        with self.assertRaises(Exception):
            evt.Parameter1 = 128

        with self.assertRaises(Exception):
            evt.Parameter2 = None
        with self.assertRaises(Exception):
            evt.Parameter2 = -1
        with self.assertRaises(Exception):
            evt.Parameter2 = 128

    def test_message(self):
        evt = ControlEvent(1, 2)
        self.assertEqual(evt.Message, [0xB0, 1, 2])


if (__name__ == '__main__'):
    unittest.main()
