#
#   test_midi_chunk_reader.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import io
import struct
import unittest
from crest.filing.midi.chunk import MidiChunk, MidiChunkReader


class TestMidiChunkReader(unittest.TestCase):
    def test_ctor(self):
        with self.assertRaises(Exception):
            MidiChunkReader(None)

    def test_mthd_chunk(self):
        chunk_content_bytes = struct.pack('>HHH', 1, 16, 480)
        chunk_bytes = b'MThd' + struct.pack('>I', 6) + chunk_content_bytes
        mcr = MidiChunkReader.CreateFromBytes(chunk_bytes)

        chunk = mcr.ReadChunk()
        self.assertTrue(isinstance(chunk, MidiChunk))
        self.assertEqual(chunk.ChunkType, b'MThd')
        self.assertEqual(chunk.Content, chunk_content_bytes)

        chunk = mcr.ReadChunk()
        self.assertEqual(chunk, None)
        self.assertEqual(mcr.ReachEnd(), True)

    def test_mtrk_chunk(self):
        chunk_content_bytes = b'CAFEBABE'
        chunk_bytes = b'MTrk' + struct.pack('>I', 8) + chunk_content_bytes
        mcr = MidiChunkReader.CreateFromBytes(chunk_bytes + chunk_bytes)

        chunks = mcr.Read()
        self.assertEqual(len(chunks), 2)
        for i in range(2):
            chunk = chunks[i]
            self.assertTrue(isinstance(chunk, MidiChunk))
            self.assertEqual(chunk.ChunkType, b'MTrk')
            self.assertEqual(chunk.Content, chunk_content_bytes)

if (__name__ == '__main__'):
    unittest.main()
