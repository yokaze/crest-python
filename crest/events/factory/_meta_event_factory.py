#
#   _meta_event_factory.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import array
import codecs
import platform

from crest.events.factory._abstract_event_factory import AbstractEventFactory
from crest.events.factory._convert_result import ConvertResult
from crest.events.meta._copyright_event import CopyrightEvent
from crest.events.meta._end_of_track_event import EndOfTrackEvent
from crest.events.meta._instrument_name_event import InstrumentNameEvent
from crest.events.meta._key_signature_event import KeySignatureEvent
from crest.events.meta._lyric_event import LyricEvent
from crest.events.meta._marker_event import MarkerEvent
from crest.events.meta._port_event import PortEvent
from crest.events.meta._tempo_event import TempoEvent
from crest.events.meta._text_event import TextEvent
from crest.events.meta._time_signature_event import TimeSignatureEvent
from crest.events.meta._track_name_event import TrackNameEvent
from crest.events.meta._unknown_meta_event import UnknownMetaEvent


class MetaEventFactory(AbstractEventFactory):
    def __init__(self, encoding='ascii'):
        super(MetaEventFactory, self).__init__()
        self.__SetEncoding(encoding)

    def Input(self, tick, message):
        status = message[0]
        if (status != 0xFF):
            return ConvertResult(False)
        number = message[1]
        length = message[2]
        if (0 < length):
            content = message[3:]
        else:
            content = None

        if (number == TextEvent.EventNumber()):
            # 0x01
            txt = self.__GetText(content)
            evt = TextEvent(txt, self.__encoding)
        elif (number == CopyrightEvent.EventNumber()):
            # 0x02
            txt = self.__GetText(content)
            evt = CopyrightEvent(txt, self.__encoding)
        elif (number == TrackNameEvent.EventNumber()):
            # 0x03
            txt = self.__GetText(content)
            evt = TrackNameEvent(txt, self.__encoding)
        elif (number == InstrumentNameEvent.EventNumber()):
            # 0x04
            txt = self.__GetText(content)
            evt = InstrumentNameEvent(txt, self.__encoding)
        elif (number == LyricEvent.EventNumber()):
            # 0x05
            txt = self.__GetText(content)
            evt = LyricEvent(txt, self.__encoding)
        elif (number == MarkerEvent.EventNumber()):
            txt = self.__GetText(content)
            # 0x06
            evt = MarkerEvent(txt, self.__encoding)
        elif (number == PortEvent.EventNumber()):
            # 0x21
            evt = PortEvent(content[0])
        elif (number == EndOfTrackEvent.EventNumber()):
            # 0x2F
            evt = EndOfTrackEvent()
        elif (number == TempoEvent.EventNumber()):
            # 0x51
            evt = TempoEvent()
            evt.MicroSeconds = (content[0] << 16) + (content[1] << 8) + content[2]
        elif (number == TimeSignatureEvent.EventNumber()):
            # 0x58
            evt = TimeSignatureEvent(content[0], 1 << content[1])
        elif (number == KeySignatureEvent.EventNumber()):
            # 0x59
            sharpNumber = content[0] if (content[0] < 128) else content[0] - 256
            isMinor = True if (content[1] != 0) else False
            evt = KeySignatureEvent(sharpNumber, isMinor)
        else:
            evt = UnknownMetaEvent(number, content)

        evt.Tick = tick
        return ConvertResult(True, evt)

    def Finalize(self):
        return ConvertResult(False)

    def __GetEncoding(self):
        return self.__encoding

    def __SetEncoding(self, encoding):
        self.__encoding = encoding

    def __GetText(self, content):
        if (content is None):
            return ''
        else:
            if (platform.python_version_tuple()[0] == '2'):
                arr = array.array('B', content).tostring()
            else:
                arr = array.array('B', content).tobytes()
            return codecs.decode(arr, self.__encoding, 'ignore')

    Encoding = property(__GetEncoding)
