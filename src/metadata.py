class Metadata:
    def __init__(self):
        self.metadata_store = []

    def save_metadata(self, chunk_info):
        self.metadata_store.append(chunk_info)

    def load_metadata(self):
        return self.metadata_store

    def get_chunk_info(self, chunk_filename):
        for info in self.metadata_store:
            if info['chunk_filename'] == chunk_filename:
                return info
        return None