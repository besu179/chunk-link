class ChunkLinkApp:
    def __init__(self, file_path, chunk_size):
        self.file_path = file_path
        self.chunk_size = chunk_size
        self.chunker = Chunker()
        self.metadata = Metadata()
        self.reconstructor = Reconstructor()

    def run(self):
        # Split the file into chunks
        chunks = self.chunker.split_file(self.file_path, self.chunk_size)
        
        # Save metadata for each chunk
        for chunk in chunks:
            chunk_info = {
                'chunk_filename': chunk,
                'chunk_size': self.chunker.get_chunk_size(chunk),
                'chunk_hash': self.chunker.get_chunk_hash(chunk)
            }
            self.metadata.save_metadata(chunk_info)

        # Reconstruct the original file
        self.reconstructor.merge_chunks('reconstructed_file')

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Chunk-Link Application')
    parser.add_argument('file_path', type=str, help='Path to the large file to be chunked')
    parser.add_argument('chunk_size', type=int, help='Size of each chunk in bytes')
    args = parser.parse_args()

    app = ChunkLinkApp(args.file_path, args.chunk_size)
    app.run()