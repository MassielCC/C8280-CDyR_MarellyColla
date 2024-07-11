import os
class FileStorage:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        os.makedirs(root_dir, exist_ok=True)
    def write(self, path, data):
        with open(os.path.join(self.root_dir, path), 'w') as f:
            f.write(data)
    def read(self, path):
        with open(os.path.join(self.root_dir, path), 'r') as f:
            return f.read()

file_storage = FileStorage('/tmp/filestorage')
file_storage.write('example.txt', 'Hello, File Storage!')
print(file_storage.read('example.txt')) 