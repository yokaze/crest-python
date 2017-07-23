#
#   _midi_file_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#


class MidiFileEvent(object):
    def __init__(self, tick, message):
        self.__tick = int(tick)
        self.__message = message

    def __GetTick(self):
        return self.__tick

    def __GetMessage(self):
        return self.__message

    Tick = property(__GetTick)
    Message = property(__GetMessage)
