# Chunk-Link Application

#### Video Demo:  <URL (https://youtu.be/r9V_82lgPaQ?si=GOLpa5Pz_jYWKF1Y)>


Chunk-Link is a Python application designed to split large files into smaller, manageable chunks, store metadata for each chunk, and reconstruct the original file from these chunks. This tool is particularly useful for handling large files in environments with storage or transmission limitations.

## Features

- Split large files into smaller chunks.
- Store metadata for each chunk, including filename, size, and hash.
- Reconstruct the original file from the stored chunks.
- Verify the integrity of chunks during reconstruction.

## Installation

To install the necessary dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

1. **Chunking a File**: Use the `Chunker` class from `chunker.py` to split a file into smaller chunks. Specify the file path and desired chunk size.

2. **Storing Metadata**: The `Metadata` class in `metadata.py` handles the storage and retrieval of metadata for each chunk.

3. **Reconstructing the File**: Use the `Reconstructor` class from `reconstruct.py` to read the chunks from a specified directory, verify their integrity, and merge them back into the original file.

## Example

```python
from src.chunker import Chunker
from src.metadata import Metadata
from src.reconstruct import Reconstructor

# Create a Chunker instance
chunker = Chunker()
chunker.split_file('large_file.txt', 1024 * 1024)  # Split into 1MB chunks

# Create a Metadata instance
metadata = Metadata()
metadata.save_metadata(chunk_info)  # Save chunk metadata

# Create a Reconstructor instance
reconstructor = Reconstructor()
reconstructor.merge_chunks('output_file.txt')  # Reconstruct the original file
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
