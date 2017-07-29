#
#   test_channel_pressure_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events import ChannelPressureEvent


class TestChannelPressureEvent(unittest.TestCase):
    def test_ctor(self):
        ChannelPressureEvent()
        ChannelPressureEvent(10)

    def test_message(self):
        evt = ChannelPressureEvent()
        self.assertEqual(evt.Message, [0xD0, 0])
        evt = ChannelPressureEvent(7)
        self.assertEqual(evt.Message, [0xD0, 7])

    def test_property(self):
        evt = ChannelPressureEvent()
        evt.Value = 7
        self.assertEqual(evt.Parameter, 7)

if (__name__ == '__main__'):
    unittest.main()
