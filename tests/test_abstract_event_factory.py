#
#   test_abstract_event_factory.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events.factory import AbstractEventFactory


class TestAbstractEventFactory(unittest.TestCase):
    def test_ctor(self):
        with self.assertRaises(TypeError):
            AbstractEventFactory()


if (__name__ == '__main__'):
    unittest.main()
