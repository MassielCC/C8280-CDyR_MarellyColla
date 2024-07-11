#Simula el almacenamiento de objetos usando un diccionario
class ObjectStorage:
    def __init__(self):
        self.storage = {}
    
    def put_object(self, key, data):
        self.storage[key] = data
    def get_object(self, key):
        return self.storage.get(key, None)

object_storage = ObjectStorage()
object_storage.put_object('file1.txt', 'Hello, Object Storage!')
print(object_storage.get_object('file1.txt')) # Output: 'Hello, Object Storage!'