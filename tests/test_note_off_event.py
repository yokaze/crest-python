#
#   test_note_off_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events import NoteOffEvent


class TestNoteOffEvent(unittest.TestCase):
    def test_ctor(self):
        NoteOffEvent()
        NoteOffEvent(10)
        NoteOffEvent(10, 20)

    def test_message(self):
        evt = NoteOffEvent()
        self.assertEqual(evt.Message, [0x80, 0, 0])
        evt = NoteOffEvent(7)
        self.assertEqual(evt.Message, [0x80, 7, 0])
        evt = NoteOffEvent(3, 7)
        self.assertEqual(evt.Message, [0x80, 3, 7])

    def test_property(self):
        evt = NoteOffEvent()
        evt.Note = 96
        evt.NoteOffVelocity = 100
        self.assertEqual(evt.Parameter1, 96)
        self.assertEqual(evt.Parameter2, 100)

if (__name__ == '__main__'):
    unittest.main()
