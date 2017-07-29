#
#   _tempo_event.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from ._meta_event import MetaEvent


class TempoEvent(MetaEvent):
    def __init__(self, tempo=120):
        super(TempoEvent, self).__init__()
        self.__SetTempo(tempo)

    def _EventNumber(self):
        return TempoEvent.EventNumber()

    def _EventContent(self):
        micro = self.MicroSeconds
        return [micro >> 16, (micro >> 8) & 0xFF, micro & 0xFF]

    def __GetTempo(self):
        return self.__tempo

    def __SetTempo(self, tempo):
        self.__tempo = int(round(tempo))

    def __GetMicroSeconds(self):
        return int(round(60. / float(self.__tempo) * 1000. * 1000.))

    def __SetMicroSeconds(self, microSeconds):
        self.__SetTempo(60. * 1000. * 1000. / float(microSeconds))

    Tempo = property(__GetTempo, __SetTempo)
    MicroSeconds = property(__GetMicroSeconds, __SetMicroSeconds)

    @staticmethod
    def EventNumber():
        return 0x51
