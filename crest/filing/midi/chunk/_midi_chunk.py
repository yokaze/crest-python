#
#   _midi_chunk.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#


class MidiChunk(object):
    def __init__(self, chunkType, content):
        if ((chunkType != b'MThd') and (chunkType != b'MTrk')):
            raise ValueError('chunkType should be MThd or MTrk.')
        if (not (type(content) == bytes)):
            raise ValueError('content should be bytes.')
        if ((chunkType == b'MThd') and (len(content) != 6)):
            raise ValueError('MThd chunk should consists of six bytes.')

        self._chunkType = chunkType
        self._content = content

    def _GetChunkType(self):
        return self._chunkType

    def _GetContent(self):
        return self._content

    ChunkType = property(_GetChunkType)
    Content = property(_GetContent)
