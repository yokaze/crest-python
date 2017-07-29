#
#   _convert_result.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from .._abstract_midi_event import AbstractMidiEvent


class ConvertResult(object):
    def __init__(self, handled, events=None):
        if (type(handled) != bool):
            raise ValueError('handled should be True or False.')
        if (events is None):
            pass
        elif (isinstance(events, AbstractMidiEvent)):
            events = [events]
        elif (isinstance(events, list)):
            if (len(events) == 0):
                events = None
            else:
                for evt in events:
                    if (not isinstance(evt, AbstractMidiEvent)):
                        raise ValueError('events are supplied but has an invalid type.')
        else:
            raise ValueError('events are supplied but has an invalid type.')

        if ((handled is False) and (isinstance(events, list))):
            if (0 < len(events)):
                raise ValueError('events are specified while handled flag is set to be False.')

        self.__handled = handled
        self.__events = events

    def __GetHandled(self):
        return self.__handled

    def __GetEvents(self):
        return self.__events

    Handled = property(__GetHandled)
    Events = property(__GetEvents)
