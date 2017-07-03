#
#   test_midi_chunk_writer.py
#   crest-python
#
#   Copyright (C) 2017 Rue Yokaze
#   Distributed under the MIT License.
#
import crest_loader
import unittest
from crest.filing.midi.chunk import MidiChunk, MidiChunkReader, MidiChunkWriter


class TestMidiChunkWriter(unittest.TestCase):
    def test_ctor(self):
        with self.assertRaises(Exception):
            MidiChunkWriter(None)

    def test_mthd_chunk(self):
        chunk_content_bytes = b'\0\1\0\x10\x01\xE0'
        chunk = MidiChunk(b'MThd', chunk_content_bytes)

        mcw = MidiChunkWriter.CreateWithBytesIO()
        mcw.WriteChunk(chunk)
        chunk_io = mcw.Output
        chunk_io.seek(0)

        mcr = MidiChunkReader(chunk_io)
        chunk = mcr.ReadChunk()
        self.assertEqual(chunk.ChunkType, b'MThd')
        self.assertEqual(chunk.Content, chunk_content_bytes)

    def test_mtrk_chunk(self):
        chunk_content_bytes = b'CAFEBABE'
        chunk = MidiChunk(b'MTrk', chunk_content_bytes)

        mcw = MidiChunkWriter.CreateWithBytesIO()
        mcw.WriteChunk(chunk)
        mcw.WriteChunk(chunk)
        chunk_io = mcw.Output
        chunk_io.seek(0)

        mcr = MidiChunkReader(chunk_io)
        chunks = mcr.Read()
        self.assertEqual(len(chunks), 2)
        for i in range(2):
            chunk = chunks[i]
            self.assertTrue(isinstance(chunk, MidiChunk))
            self.assertEqual(chunk.ChunkType, b'MTrk')
            self.assertEqual(chunk.Content, chunk_content_bytes)
