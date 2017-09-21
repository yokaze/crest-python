#
#   test_note_on_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events import NoteOnEvent


class TestNoteOnEvent(unittest.TestCase):
    def test_ctor(self):
        NoteOnEvent()
        NoteOnEvent(10)
        NoteOnEvent(10, 20)

    def test_message(self):
        evt = NoteOnEvent()
        self.assertEqual(evt.Message, [0x90, 0, 0])
        evt = NoteOnEvent(7)
        self.assertEqual(evt.Message, [0x90, 7, 0])
        evt = NoteOnEvent(3, 7)
        self.assertEqual(evt.Message, [0x90, 3, 7])

    def test_property(self):
        evt = NoteOnEvent()
        evt.Note = 96
        evt.Velocity = 100
        self.assertEqual(evt.Parameter1, 96)
        self.assertEqual(evt.Parameter2, 100)


if (__name__ == '__main__'):
    unittest.main()
