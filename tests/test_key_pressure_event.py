#
#   test_key_pressure_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events import KeyPressureEvent


class TestKeyPressureEvent(unittest.TestCase):
    def test_ctor(self):
        KeyPressureEvent()
        KeyPressureEvent(10)
        KeyPressureEvent(10, 20)

    def test_message(self):
        evt = KeyPressureEvent()
        self.assertEqual(evt.Message, [0xA0, 0, 0])
        evt = KeyPressureEvent(7)
        self.assertEqual(evt.Message, [0xA0, 7, 0])
        evt = KeyPressureEvent(3, 7)
        self.assertEqual(evt.Message, [0xA0, 3, 7])

    def test_property(self):
        evt = KeyPressureEvent()
        evt.Note = 96
        evt.Value = 32
        self.assertEqual(evt.Parameter1, 96)
        self.assertEqual(evt.Parameter2, 32)

if (__name__ == '__main__'):
    unittest.main()
