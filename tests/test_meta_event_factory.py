#
#   test_meta_event_factory.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.events.factory import ConvertResult
from crest.events.factory import MetaEventFactory
from crest.events.meta import CopyrightEvent
from crest.events.meta import EndOfTrackEvent
from crest.events.meta import InstrumentNameEvent
from crest.events.meta import KeySignatureEvent
from crest.events.meta import LyricEvent
from crest.events.meta import MarkerEvent
from crest.events.meta import PortEvent
from crest.events.meta import TextEvent
from crest.events.meta import TempoEvent
from crest.events.meta import TimeSignatureEvent
from crest.events.meta import TrackNameEvent
from crest.events.meta import UnknownMetaEvent


class TestMetaEventFactory(unittest.TestCase):
    def test_ctor(self):
        MetaEventFactory()

    def test_channel_event(self):
        factory = MetaEventFactory()
        cr = factory.Input(0, [0x90, 0x40, 0x40])
        self.assertTrue(isinstance(cr, ConvertResult))
        self.assertEqual(cr.Handled, False)
        self.assertEqual(cr.Events, None)

    def test_result_format(self):
        factory = MetaEventFactory()
        cr = factory.Input(0, [0xFF, 0x2F, 0x00])
        self.assertTrue(isinstance(cr, ConvertResult))
        self.assertEqual(cr.Handled, True)
        self.assertEqual(type(cr.Events), list)
        self.assertTrue(isinstance(cr.Events[0], EndOfTrackEvent))

    def test_tick(self):
        factory = MetaEventFactory()
        cr = factory.Input(100, [0xFF, 0x2F, 0x00])
        self.assertEqual(cr.Events[0].Tick, 100)

    def test_results(self):
        factory = MetaEventFactory()

        cr = factory.Input(0, [0xFF, 0x01, 0x04, 0x74, 0x65, 0x73, 0x74])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, TextEvent))
        self.assertEqual(msg.Text, 'test')

        cr = factory.Input(0, [0xFF, 0x02, 0x04, 0x74, 0x65, 0x73, 0x74])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, CopyrightEvent))
        self.assertEqual(msg.Text, 'test')

        cr = factory.Input(0, [0xFF, 0x03, 0x04, 0x74, 0x65, 0x73, 0x74])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, TrackNameEvent))
        self.assertEqual(msg.Text, 'test')

        cr = factory.Input(0, [0xFF, 0x04, 0x04, 0x74, 0x65, 0x73, 0x74])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, InstrumentNameEvent))
        self.assertEqual(msg.Text, 'test')

        cr = factory.Input(0, [0xFF, 0x05, 0x04, 0x74, 0x65, 0x73, 0x74])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, LyricEvent))
        self.assertEqual(msg.Text, 'test')

        cr = factory.Input(0, [0xFF, 0x06, 0x04, 0x74, 0x65, 0x73, 0x74])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, MarkerEvent))
        self.assertEqual(msg.Text, 'test')

        cr = factory.Input(0, [0xFF, 0x21, 0x01, 0x04])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, PortEvent))
        self.assertEqual(msg.Port, 4)

        cr = factory.Input(0, [0xFF, 0x2F, 0x00])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, EndOfTrackEvent))

        cr = factory.Input(0, [0xFF, 0x51, 0x03, 0x07, 0xA1, 0x20])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, TempoEvent))
        self.assertEqual(msg.Tempo, 120)

        cr = factory.Input(0, [0xFF, 0x58, 0x04, 0x03, 0x04, 0x18, 0x08])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, TimeSignatureEvent))
        self.assertEqual(msg.Beat, 3)
        self.assertEqual(msg.Note, 16)

        cr = factory.Input(0, [0xFF, 0x59, 0x02, 0xFF, 0x01])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, KeySignatureEvent))
        self.assertEqual(msg.SharpNumber, -1)
        self.assertEqual(msg.IsMinor, True)

        cr = factory.Input(0, [0xFF, 0x7E, 0x03, 0x00, 0x01, 0x02])
        msg = cr.Events[0]
        self.assertTrue(isinstance(msg, UnknownMetaEvent))
        self.assertEqual(msg.EventNumber, 0x7E)
        self.assertEqual(msg.Content, [0x00, 0x01, 0x02])


if (__name__ == '__main__'):
    unittest.main()
