#
#   test_text_meta_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events.meta import TextMetaEvent


class TestTextMetaEvent(unittest.TestCase):
    def test_ctor(self):
        with self.assertRaises(TypeError):
            TextMetaEvent()

if (__name__ == '__main__'):
    unittest.main()
