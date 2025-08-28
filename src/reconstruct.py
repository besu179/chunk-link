class Reconstructor:
    def __init__(self, chunk_directory):
        self.chunk_directory = chunk_directory

    def read_chunks(self):
        import os
        chunks = []
        for filename in sorted(os.listdir(self.chunk_directory)):
            if filename.startswith("chunk_"):
                with open(os.path.join(self.chunk_directory, filename), 'rb') as chunk_file:
                    chunks.append(chunk_file.read())
        return chunks

    def verify_chunk(self, chunk, expected_hash):
        import hashlib
        chunk_hash = hashlib.sha256(chunk).hexdigest()
        return chunk_hash == expected_hash

    def merge_chunks(self, output_file):
        chunks = self.read_chunks()
        with open(output_file, 'wb') as output:
            for chunk in chunks:
                output.write(chunk)