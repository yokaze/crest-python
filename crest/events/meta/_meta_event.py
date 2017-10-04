#
#   _meta_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import abc

from crest.events._midi_event import MidiEvent


class MetaEvent(MidiEvent):
    def __init__(self):
        super(MetaEvent, self).__init__()

    @abc.abstractmethod
    def _EventNumber(self):
        pass

    @abc.abstractmethod
    def _EventContent(self):
        pass

    def __GetEventNumber(self):
        return self._EventNumber()

    def __GetMessage(self):
        eventNumber = self._EventNumber()
        eventContent = self._EventContent()
        if (eventContent is None):
            return [0xFF, eventNumber, 0]
        else:
            eventLength = len(eventContent)
            return [0xFF, eventNumber, eventLength] + eventContent

    EventNumber = property(__GetEventNumber)
    Message = property(__GetMessage)
