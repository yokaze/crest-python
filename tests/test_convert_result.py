#
#   test_convert_result.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events.factory import ConvertResult
from crest.events import NoteOnEvent


class TestConvertResult(unittest.TestCase):
    def test_ctor(self):
        with self.assertRaises(Exception):
            ConvertResult()
        with self.assertRaises(Exception):
            ConvertResult(None)
        with self.assertRaises(Exception):
            ConvertResult('success')
        with self.assertRaises(Exception):
            ConvertResult(True, 'invalid event')
        with self.assertRaises(Exception):
            ConvertResult(True, ['invalid event'])
        ConvertResult(False)
        ConvertResult(False, None)
        ConvertResult(False, [])
        ConvertResult(True)
        ConvertResult(True, None)
        ConvertResult(True, [])
        cr = ConvertResult(False, [])
        self.assertEqual(cr.Handled, False)
        self.assertEqual(cr.Events, None)
        cr = ConvertResult(True, NoteOnEvent())
        self.assertEqual(cr.Handled, True)
        self.assertTrue(isinstance(cr.Events, list))
        self.assertTrue(isinstance(cr.Events[0], NoteOnEvent))
        cr = ConvertResult(True, [NoteOnEvent()])
        self.assertEqual(cr.Handled, True)
        self.assertTrue(isinstance(cr.Events, list))
        self.assertTrue(isinstance(cr.Events[0], NoteOnEvent))


if (__name__ == '__main__'):
    unittest.main()
