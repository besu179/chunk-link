import os
import unittest
from src.chunker import Chunker

class TestChunker(unittest.TestCase):
    def setUp(self):
        self.chunker = Chunker()
        self.test_file_path = 'test_file.txt'
        self.chunk_size = 10
        
        # Create a test file
        with open(self.test_file_path, 'w') as f:
            f.write('This is a test file for chunking.')

    def tearDown(self):
        # Remove the test file and any generated chunks
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
        for i in range(3):  # Assuming 3 chunks for the test
            chunk_file = f'chunk_{i}.txt'
            if os.path.exists(chunk_file):
                os.remove(chunk_file)

    def test_split_file(self):
        chunks = self.chunker.split_file(self.test_file_path, self.chunk_size)
        self.assertEqual(len(chunks), 3)  # Expecting 3 chunks

        for i, chunk in enumerate(chunks):
            self.assertTrue(os.path.exists(chunk))
            with open(chunk, 'r') as f:
                content = f.read()
                self.assertEqual(content, 'This is a test ' if i < 2 else 'file for chunking.')

if __name__ == '__main__':
    unittest.main()