#
#   _unknown_meta_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from ._meta_event import MetaEvent


class UnknownMetaEvent(MetaEvent):
    def __init__(self, eventNumber, content=None):
        super(UnknownMetaEvent, self).__init__()
        self.__SetEventNumber(eventNumber)
        self.__SetContent(content)

    def _EventNumber(self):
        return self.__eventNumber

    def _EventContent(self):
        return self.__content

    def __GetEventNumber(self):
        return self.__eventNumber

    def __SetEventNumber(self, eventNumber):
        self.__eventNumber = eventNumber

    def __GetContent(self):
        return self.__content

    def __SetContent(self, content):
        if (content is None):
            self.__content = None
        else:
            self.__content = list(content)

    EventNumber = property(__GetEventNumber, __SetEventNumber)
    Content = property(__GetContent, __SetContent)
