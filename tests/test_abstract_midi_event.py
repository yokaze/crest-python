#
#   test_abstract_midi_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events import AbstractMidiEvent


class TestAbstractMidiEvent(unittest.TestCase):
    def test_ctor(self):
        with self.assertRaises(TypeError):
            AbstractMidiEvent()


if (__name__ == '__main__'):
    unittest.main()
