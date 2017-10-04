#
#   _two_bytes_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import abc

from .._midi_event import MidiEvent


class TwoBytesEvent(MidiEvent):
    def __init__(self, parameter=0):
        super(TwoBytesEvent, self).__init__()
        self.__SetParameter(parameter)

    def _GetMessage(self):
        body = self._StatusBase()
        ch = self.Channel
        return [body | ch, self.__parameter]

    @abc.abstractmethod
    def _StatusBase(self):
        return None

    def __GetParameter(self):
        return self.__parameter

    def __SetParameter(self, parameter):
        parameter = int(parameter)
        if ((parameter < 0) or (128 <= parameter)):
            raise ValueError('parameter should be from 0 to 127.')
        self.__parameter = parameter

    Parameter = property(__GetParameter, __SetParameter)
