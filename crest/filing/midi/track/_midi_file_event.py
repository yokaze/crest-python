#
#   _midi_file_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#


class MidiFileEvent(object):
    def __init__(self, tick, message):
        self._tick = int(tick)
        self._message = message

    def _GetTick(self):
        return self._tick

    def _GetMessage(self):
        return self._message

    Tick = property(_GetTick)
    Message = property(_GetMessage)
