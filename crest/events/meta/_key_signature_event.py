#
#   _key_signature.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
from ._meta_event import MetaEvent


class KeySignatureEvent(MetaEvent):
    def __init__(self, sharpNumber=0, isMinor=False):
        super(KeySignatureEvent, self).__init__()
        self.__SetSharpNumber(sharpNumber)
        self.__SetIsMinor(isMinor)

    def _EventNumber(self):
        return KeySignatureEvent.EventNumber()

    def _EventContent(self):
        sharpNumber = self.__sharpNumber
        if (sharpNumber < 0):
            sharpNumber += 256
        minorFlag = 1 if self.__isMinor else 0
        return [sharpNumber, minorFlag]

    def __GetSharpNumber(self):
        return self.__sharpNumber

    def __SetSharpNumber(self, sharpNumber):
        sharpNumber = int(sharpNumber)
        if ((sharpNumber < -7) or (sharpNumber > 7)):
            raise ValueError('Invalid sharp number is specified: %d' % sharpNumber)
        self.__sharpNumber = sharpNumber

    def __GetIsMinor(self):
        return self.__isMinor

    def __SetIsMinor(self, isMinor):
        self.__isMinor = bool(isMinor)

    SharpNumber = property(__GetSharpNumber, __SetSharpNumber)
    IsMinor = property(__GetIsMinor, __SetIsMinor)

    @staticmethod
    def EventNumber():
        return 0x59
