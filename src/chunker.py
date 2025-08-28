class Chunker:
    def __init__(self):
        pass

    def split_file(self, file_path, chunk_size):
        with open(file_path, 'rb') as file:
            chunk_number = 0
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                chunk_filename = f"{file_path}_chunk_{chunk_number}"
                with open(chunk_filename, 'wb') as chunk_file:
                    chunk_file.write(chunk)
                chunk_number += 1
        return chunk_number  # Return the number of chunks created