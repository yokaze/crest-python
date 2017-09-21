#
#   test_two_bytes_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events import ProgramEvent


class TestTwoBytesEvent(unittest.TestCase):
    def test_ctor(self):
        ProgramEvent()
        evt = ProgramEvent(7.)
        self.assertTrue(type(evt.Parameter) == int)
        self.assertEqual(evt.Parameter, 7)

        with self.assertRaises(Exception):
            ProgramEvent(None)
        with self.assertRaises(Exception):
            ProgramEvent(-1)
        with self.assertRaises(Exception):
            ProgramEvent(128)
        with self.assertRaises(Exception):
            ProgramEvent(0, 0)

    def test_parameter(self):
        evt = ProgramEvent()
        evt.Parameter = 2.
        self.assertTrue(type(evt.Parameter) == int)
        self.assertEqual(evt.Parameter, 2)

        with self.assertRaises(Exception):
            evt.Parameter = None
        with self.assertRaises(Exception):
            evt.Parameter = -1
        with self.assertRaises(Exception):
            evt.Parameter = 128

    def test_message(self):
        evt = ProgramEvent(7)
        self.assertEqual(evt.Message, [0xC0, 7])


if (__name__ == '__main__'):
    unittest.main()
