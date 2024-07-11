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

#Simula el manejo de permisos mediante un diccionario de permisos.
class S3BucketWithPermissions(S3Bucket):
    def __init__(self):
        super().__init__()
        self.permissions = {}
    
    def set_permission(self, bucket, key, permission):
        if bucket not in self.permissions:
            self.permissions[bucket] = {}
        self.permissions[bucket][key] = permission
    
    def check_permission(self, bucket, key, action):
        return self.permissions.get(bucket, {}).get(key) == action
    

class S3BucketWithVersioning(S3Bucket):
    def __init__(self):
        super().__init__()
        self.versions = {}
    
    def put_object(self, bucket, key, data):
        if bucket not in self.versions:
            self.versions[bucket] = {}
        
        if key not in self.versions[bucket]:
            self.versions[bucket][key] = []
        self.versions[bucket][key].append(data)

    def get_object(self, bucket, key, version=None):
        if version is None:
            return self.versions.get(bucket, {}).get(key, [])[-1]
        return self.versions.get(bucket, {}).get(key, [])[version]

# Simula la replicación de objetos entre dos buckets
class S3BucketWithReplication(S3Bucket):
    def replicate(self, source_bucket, target_bucket):
        if source_bucket in self.buckets and target_bucket in self.buckets:
            self.buckets[target_bucket] = self.buckets[source_bucket].copy()


# Ejemplo de uso
s3 = S3Bucket()
s3.create_bucket('mybucket')
s3.put_object('mybucket', 'file1.txt', 'Hello, S3 Bucket!')
print(s3.get_object('mybucket', 'file1.txt')) # Output: 'Hello, S3 Bucket!'

# Bucket con permisos
s3p = S3BucketWithPermissions()
s3p.create_bucket('mybucket')
s3p.put_object('mybucket', 'file1.txt', 'Hello, S3 with Permissions!')
s3p.set_permission('mybucket', 'file1.txt', 'read')
print(s3p.check_permission('mybucket', 'file1.txt', 'read')) # Output: True

# Bucket con versionado
s3v = S3BucketWithVersioning()
s3v.create_bucket('mybucket')
s3v.put_object('mybucket', 'file1.txt', 'Version 1')
s3v.put_object('mybucket', 'file1.txt', 'Version 2')
print(s3v.get_object('mybucket', 'file1.txt')) # Output: 'Version 2'
print(s3v.get_object('mybucket', 'file1.txt', 0)) # Output: 'Version 1'

# Ejemplo de uso
s3r = S3BucketWithReplication()
s3r.create_bucket('source_bucket')
s3r.create_bucket('target_bucket')
s3r.put_object('source_bucket', 'file1.txt', 'Data to Replicate')
s3r.replicate('source_bucket', 'target_bucket')
print(s3r.get_object('target_bucket', 'file1.txt')) # Output: 'Data to Replicate'