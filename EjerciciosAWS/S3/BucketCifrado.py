#Bucket con cifrado Fernet: cifrado simetrico
from cryptography.fernet import Fernet

# Generar una clave para el cifrado
key = Fernet.generate_key()

# Crear un objeto Fernet con la clave generada
cipher_suite = Fernet(key)

# Mensaje que deseas cifrar
message = b"Mi mensaje secreto"

# Cifrar el mensaje
cipher_text = cipher_suite.encrypt(message)

# Descifrar el mensaje
plain_text = cipher_suite.decrypt(cipher_text)

# Imprimir los resultados
print("Mensaje original:", message.decode())
print("Mensaje cifrado:", cipher_text)
print("Mensaje descifrado:", plain_text.decode())

#Encriptación de objetos--------------------------------------
from cryptography.fernet import Fernet
class S3Bucket:
    def __init__(self):
        self.buckets = {}

    def create_bucket(self, name):
        self.buckets[name] = {}
    
    def put_object(self, bucket, key, data):
        if bucket in self.buckets:
            self.buckets[bucket][key] = data
    
    def get_object(self, bucket, key):
        return self.buckets.get(bucket, {}).get(key, None)
    
class S3BucketWithEncryption(S3Bucket):
    def __init__(self, key):
        super().__init__()
        self.cipher = Fernet(key)
    
    def put_object(self, bucket, key, data):
        encrypted_data = self.cipher.encrypt(data.encode())
        super().put_object(bucket, key, encrypted_data)
    def get_object(self, bucket, key):
        encrypted_data = super().get_object(bucket, key)
        return self.cipher.decrypt(encrypted_data).decode()

key = Fernet.generate_key()
s3e = S3BucketWithEncryption(key)
s3e.create_bucket('mybucket')
s3e.put_object('mybucket', 'file1.txt', 'Encrypted Data')
print(s3e.get_object('mybucket', 'file1.txt')) # Output: 'Encrypted Data'
