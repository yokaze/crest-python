#
#   test_single_event_factory.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events import ChannelPressureEvent
from crest.events import ControlEvent
from crest.events import ExclusiveEvent
from crest.events import KeyPressureEvent
from crest.events import NoteOffEvent
from crest.events import NoteOnEvent
from crest.events import PitchEvent
from crest.events import ProgramEvent
from crest.events.factory import ConvertResult
from crest.events.factory import SingleEventFactory
from crest.events.meta import EndOfTrackEvent

class TestSingleEventFactory(unittest.TestCase):
    def test_ctor(self):
        SingleEventFactory()

    def test_tick(self):
        factory = SingleEventFactory()
        cr = factory.Input(500, [0x90, 0x40, 0x40])
        self.assertEqual(cr.Events[0].Tick, 500)

    def test_channel_event(self):
        factory = SingleEventFactory()

        cr = factory.Input(0, [0x80, 0x40, 0x60])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, NoteOffEvent))
        self.assertTrue(msg.Note, 0x40)
        self.assertTrue(msg.NoteOffVelocity, 0x60)

        cr = factory.Input(0, [0x90, 0x40, 0x60])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, NoteOnEvent))
        self.assertTrue(msg.Note, 0x40)
        self.assertTrue(msg.Velocity, 0x60)

        cr = factory.Input(0, [0xA0, 0x40, 0x60])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, KeyPressureEvent))
        self.assertEqual(msg.Note, 0x40)
        self.assertEqual(msg.Value, 0x60)

        cr = factory.Input(0, [0xB0, 0x07, 0x50])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, ControlEvent))
        self.assertEqual(msg.Number, 0x07)
        self.assertEqual(msg.Value, 0x50)

        cr = factory.Input(0, [0xC0, 0x40])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, ProgramEvent))
        self.assertEqual(msg.Value, 0x40)

        cr = factory.Input(0, [0xD0, 0x40])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, ChannelPressureEvent))
        self.assertEqual(msg.Value, 0x40)

        cr = factory.Input(0, [0xE0, 0x60, 0x20])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, PitchEvent))
        self.assertEqual(msg.Value, 0x1020)

        cr = factory.Input(0, [0xF0, 0x01, 0x02, 0xF7])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, ExclusiveEvent))
        self.assertEqual(msg.Content, [0xF0, 0x01, 0x02, 0xF7])

        factory = SingleEventFactory()
        cr = factory.Input(0, [0xFF, 0x2F, 0x00])
        self.assertTrue(isinstance(cr.Events[0], EndOfTrackEvent))

if (__name__ == '__main__'):
    unittest.main()
