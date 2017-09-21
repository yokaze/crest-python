#
#   _test_end_of_track_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events.meta import EndOfTrackEvent


class TestEndOfTrackEvent(unittest.TestCase):
    def test_ctor(self):
        EndOfTrackEvent()

    def test_message(self):
        evt = EndOfTrackEvent()
        self.assertEqual(evt.Message, [0xFF, 0x2F, 0x00])


if (__name__ == '__main__'):
    unittest.main()
