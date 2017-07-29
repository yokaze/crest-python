#
#   _abstract_event_factory.py
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


class AbstractEventFactory(ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def Input(self, tick, message):
        pass

    @abc.abstractmethod
    def Finalize(self, tick, message):
        pass
