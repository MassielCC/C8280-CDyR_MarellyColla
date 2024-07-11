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


class ObjectStorageWithPolicies(S3Bucket):
    def __init__(self):
        super().__init__()
        self.policies=[]

    def put_object(self, bucket, key, data, role):
        if bucket in self.buckets:
            self.buckets[bucket][key] = data
    
    def get_object(self, bucket, key, role):
        return self.buckets.get(bucket, {}).get(key, None)

    def define_policy(self,role,action, resorce):
        policy={
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": role,
                    "Action": action,
                    "Resource": resorce
                }
            ]
        }
        self.policies.append({role:policy})
        print(policy)


