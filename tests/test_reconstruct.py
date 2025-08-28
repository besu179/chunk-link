import os
import unittest
from src.reconstruct import Reconstructor

class TestReconstructor(unittest.TestCase):

    def setUp(self):
        self.reconstructor = Reconstructor()
        self.chunk_directory = 'test_chunks'
        os.makedirs(self.chunk_directory, exist_ok=True)
        self.create_test_chunks()

    def create_test_chunks(self):
        for i in range(3):
            with open(os.path.join(self.chunk_directory, f'chunk_{i}.txt'), 'w') as f:
                f.write(f'This is chunk {i}.')

    def test_read_chunks(self):
        chunks = self.reconstructor.read_chunks(self.chunk_directory)
        self.assertEqual(len(chunks), 3)
        self.assertEqual(chunks[0], 'This is chunk 0.')
        self.assertEqual(chunks[1], 'This is chunk 1.')
        self.assertEqual(chunks[2], 'This is chunk 2.')

    def test_verify_chunk(self):
        chunk_path = os.path.join(self.chunk_directory, 'chunk_0.txt')
        self.assertTrue(self.reconstructor.verify_chunk(chunk_path))

    def test_merge_chunks(self):
        output_file = 'reconstructed_file.txt'
        self.reconstructor.merge_chunks(output_file)
        with open(output_file, 'r') as f:
            content = f.read()
        expected_content = 'This is chunk 0.This is chunk 1.This is chunk 2.'
        self.assertEqual(content, expected_content)

    def tearDown(self):
        for i in range(3):
            os.remove(os.path.join(self.chunk_directory, f'chunk_{i}.txt'))
        os.rmdir(self.chunk_directory)
        if os.path.exists('reconstructed_file.txt'):
            os.remove('reconstructed_file.txt')

if __name__ == '__main__':
    unittest.main()