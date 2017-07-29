#
#   _exclusive_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from ._midi_event import MidiEvent


class ExclusiveEvent(MidiEvent):
    def __init__(self, content):
        super(ExclusiveEvent, self).__init__()
        self.__SetContent(content)

    def _GetMessage(self):
        return self.__content

    def __GetContent(self):
        return self.__content

    def __SetContent(self, content):
        if (content is None):
            self.__content = None
        else:
            self.__content = list(content)

    Content = property(__GetContent, __SetContent)
