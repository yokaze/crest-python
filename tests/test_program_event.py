#
#   test_program_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events import ProgramEvent


class TestProgramEvent(unittest.TestCase):
    def test_ctor(self):
        ProgramEvent()
        ProgramEvent(10)

    def test_message(self):
        evt = ProgramEvent()
        self.assertEqual(evt.Message, [0xC0, 0])
        evt = ProgramEvent(7)
        self.assertEqual(evt.Message, [0xC0, 7])

    def test_property(self):
        evt = ProgramEvent()
        evt.Value = 7
        self.assertEqual(evt.Parameter, 7)


if (__name__ == '__main__'):
    unittest.main()
