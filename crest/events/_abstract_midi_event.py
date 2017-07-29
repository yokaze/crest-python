#
#   _abstract_midi_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import abc
import platform

if (platform.python_version_tuple()[0] == '2'):
    class ABC(object):
        __metaclass__ = abc.ABCMeta
else:
    ABC = abc.ABC


class AbstractMidiEvent(ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def _GetChannel(self):
        pass

    @abc.abstractmethod
    def _SetChannel(self, channel):
        pass

    @abc.abstractmethod
    def _GetTick(self):
        pass

    @abc.abstractmethod
    def _SetTick(self, tick):
        pass

    def _GetMessage(self):
        return None

    def __GetChannel(self):
        return self._GetChannel()

    def __SetChannel(self, channel):
        self._SetChannel(channel)

    def __GetTick(self):
        return self._GetTick()

    def __SetTick(self, tick):
        self._SetTick(tick)

    def __GetMessage(self):
        return self._GetMessage()

    Channel = property(__GetChannel, __SetChannel)
    Tick = property(__GetTick, __SetTick)
    Message = property(__GetMessage)
