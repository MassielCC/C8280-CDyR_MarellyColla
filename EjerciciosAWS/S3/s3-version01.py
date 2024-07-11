import os

#Crear un archivo para almacenar en el bucket
def crear_file(bucket, nombre, contenido):
    ruta= "./buckets/" +  bucket
    if os.path.exists(ruta):
        ruta2= ruta +  "/" + nombre
        with open(ruta2, "w") as archivoI:
            archivoI.write(contenido)
        archivoI.close()
    else:
        print("Ruta no encontrada")

class S3Bucket:
    def __init__(self):
        self.buckets = {}

    #Método para crear bucket
    def create_bucket(self, name):
        self.buckets[name] = {}
        # Crear un directorio con el name
        ruta = './buckets/' + name
        # verificar si el directorio ya existe
        if not os.path.exists(ruta):
            os.mkdir(ruta)
            print("Directorio %s creado!" % ruta)
        else:
            print("Directorio %s ya existe" % ruta)

    #Cargar un objeto al bucket
    def put_object(self, bucket, key, data):
        if bucket in self.buckets:
            self.buckets[bucket][key] = data

            #Crear el archivo en el bucket
            crear_file(bucket, key, data)

    #Metodo  para mostrar el objeto
    def get_object(self, bucket, key):
        return self.buckets.get(bucket, {}).get(key, None)
    
class S3BucketWithVersioning(S3Bucket):
    def __init__(self):
        super().__init__()
        self.versions = {}

    #Método para crear versiones del objeto
    def put_object(self, bucket, key, data):
        #si el objeto no ha sido creado, se crea como key
        if bucket not in self.versions:
            self.versions[bucket] = {}

        #si el objeto no tiene ninguna versión, se le asigna una lista vacia
        if key not in self.versions[bucket]:
            self.versions[bucket][key] = []
            crear_file(bucket, key, data)
        else:
            n=len(self.versions[bucket][key])+1
            nuevo_id= key[:-4] + "_v" + str(n) + ".txt"
            crear_file(bucket, nuevo_id, data)

        #se guardan todas las versiones en la lista previamente creada
        self.versions[bucket][key].append(data)

    #Método para mostrar versiones del objeto
    def get_object(self, bucket, key, version=None):
        #Devuelve la última versión si no se especifica uno
        if version is None:
            return self.versions.get(bucket, {}).get(key, [])[-1]
        return self.versions.get(bucket, {}).get(key, [])[version]


# Ejemplo de uso
s3=S3Bucket()
s3.create_bucket('mybucket')
s3.put_object('mybucket', 'file1.txt', 'Hello, S3 Bucket sin versionado!')
s3.put_object('mybucket', 'file2.txt', 'S3 Bucket 2do objeto!')
print("Contenido del bucket: ", s3.buckets )
name_objeto=input("Archivo: ")
print("Contenido de objeto: ", s3.get_object('mybucket', name_objeto),  "\n")

#Ejemplo con versionado
s3v = S3BucketWithVersioning()
s3v.create_bucket('bucketVersionado')
s3v.put_object('bucketVersionado', 'file1.txt', 'Hola soy la Version 1')
s3v.put_object('bucketVersionado', 'file2.txt', 'Este es otro objeto')
s3v.put_object('bucketVersionado', 'file1.txt', 'Hola, esta es la version 2')
print("Contenido del bucket: ", s3v.versions, "\n" )

print(s3v.get_object('bucketVersionado', 'file1.txt')) # Output: 'Version 2'
print(s3v.get_object('bucketVersionado', 'file1.txt', 0)) # Output: 'Version 1'

