#
#   _three_bytes_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import abc

from .._midi_event import MidiEvent


class ThreeBytesEvent(MidiEvent):
    def __init__(self, parameter1=0, parameter2=0):
        super(ThreeBytesEvent, self).__init__()
        self.__SetParameter1(parameter1)
        self.__SetParameter2(parameter2)

    def _GetMessage(self):
        body = self._StatusBase()
        ch = self.Channel
        return [body | ch, self.__parameter1, self.__parameter2]

    @abc.abstractmethod
    def _StatusBase(self):
        pass

    def __GetParameter1(self):
        return self.__parameter1

    def __SetParameter1(self, parameter):
        parameter = int(parameter)
        if ((parameter < 0) or (128 <= parameter)):
            raise ValueError('parameter should be from 0 to 127.')
        self.__parameter1 = parameter

    def __GetParameter2(self):
        return self.__parameter2

    def __SetParameter2(self, parameter):
        parameter = int(parameter)
        if ((parameter < 0) or (128 <= parameter)):
            raise ValueError('parameter should be from 0 to 127.')
        self.__parameter2 = parameter

    Parameter1 = property(__GetParameter1, __SetParameter1)
    Parameter2 = property(__GetParameter2, __SetParameter2)
