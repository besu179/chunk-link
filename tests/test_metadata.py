import unittest
from src.metadata import Metadata

class TestMetadata(unittest.TestCase):

    def setUp(self):
        self.metadata = Metadata()
        self.chunk_info = {
            'chunk_filename': 'chunk_1.dat',
            'chunk_size': 1024,
            'chunk_hash': 'abc123'
        }

    def test_save_metadata(self):
        self.metadata.save_metadata(self.chunk_info)
        loaded_metadata = self.metadata.load_metadata()
        self.assertEqual(loaded_metadata['chunk_filename'], self.chunk_info['chunk_filename'])
        self.assertEqual(loaded_metadata['chunk_size'], self.chunk_info['chunk_size'])
        self.assertEqual(loaded_metadata['chunk_hash'], self.chunk_info['chunk_hash'])

    def test_load_metadata_empty(self):
        self.metadata.save_metadata({})
        loaded_metadata = self.metadata.load_metadata()
        self.assertEqual(loaded_metadata, {})

if __name__ == '__main__':
    unittest.main()