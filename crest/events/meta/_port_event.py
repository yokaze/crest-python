#
#   _port_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from crest.events.meta._meta_event import MetaEvent


class PortEvent(MetaEvent):
    def __init__(self, port=0):
        super(PortEvent, self).__init__()
        self.__SetPort(port)

    def _EventNumber(self):
        return PortEvent.EventNumber()

    def _EventContent(self):
        return [self.__port]

    def __GetPort(self):
        return self.__port

    def __SetPort(self, port):
        port = int(port)
        self.__port = port

    Port = property(__GetPort, __SetPort)

    @staticmethod
    def EventNumber():
        return 0x21
