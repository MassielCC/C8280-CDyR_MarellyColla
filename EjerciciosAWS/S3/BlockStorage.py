#Simula un almacenamiento en bloque con archivos binarios en Python
class BlockStorage:
    def __init__(self, size):
        self.storage = bytearray(size)
    def write(self, data, offset):
        self.storage[offset:offset+len(data)] = data
    def read(self, offset, size):
        return self.storage[offset:offset+size]

# Ejemplo de uso
block_storage = BlockStorage(1024)
block_storage.write(b"Hello", 0)
print(block_storage.read(0, 5)) # Output: b'Hello'