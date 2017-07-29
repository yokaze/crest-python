#
#   test_key_signature_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events.meta import KeySignatureEvent


class TestKeySignatureEvent(unittest.TestCase):
    def test_ctor(self):
        KeySignatureEvent()
        KeySignatureEvent(3)
        KeySignatureEvent(3, True)

    def test_message(self):
        evt = KeySignatureEvent(3, True)
        self.assertEqual(evt.Message, [0xFF, 0x59, 0x02, 0x03, 0x01])
        evt = KeySignatureEvent(-1, False)
        self.assertEqual(evt.Message, [0xFF, 0x59, 0x02, 0xFF, 0x00])

    def test_property(self):
        evt = KeySignatureEvent()
        evt.SharpNumber = 3
        evt.IsMinor = True
        self.assertEqual(evt.SharpNumber, 3)
        self.assertEqual(evt.IsMinor, True)

if (__name__ == '__main__'):
    unittest.main()
