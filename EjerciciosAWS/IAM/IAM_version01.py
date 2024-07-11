import random

# Simular configuración de MFA con código de verificación
def setup_mfa(user_name):
    code = random.randint(100000, 999999)
    print(f"MFA setup for user '{user_name}'. Verification code: {code}")

def crear_json_policy(action="s3:ListBucket"):
    example_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
            "Effect": "Allow",
            "Action": action,
            "Resource": "arn:aws:s3:::example_bucket"
            }
        ]
    }
    return example_policy

def set_password_policy(min_length, require_symbols, require_numbers):
    policy = {
        "min_length": min_length,
        "require_symbols": require_symbols,
        "require_numbers": require_numbers
        }
    print("Password policy set:", policy)

class IAMService:
    def __init__(self):
        self.users = {} 
        self.groups = {}
        self.policies = {}
        self.roles = {}
        
    #Método para crear usuario
    def create_user(self, iam_service, user_name):
        iam_service.users[user_name] = {'policies': [], 'mfa_enabled': False}
        print(f"User '{user_name}' created.")

    def create_group(self, iam_service, group_name):
        iam_service.groups[group_name] = {'policies': [], 'users': []}
        print(f"Group '{group_name}' created.")

    def add_user_to_group(self, iam_service, user_name, group_name):
        if user_name in iam_service.users and group_name in iam_service.groups:
            iam_service.groups[group_name]['users'].append(user_name)
            print(f"User '{user_name}' added to group '{group_name}'.")
    
    def assign_policy_to_user(self, iam_service, user_name, policy):
        if user_name in iam_service.users:
            iam_service.users[user_name]['policies'].append(policy)
            print(f"Policy assigned to user '{user_name}'.")
    
    def assign_policy_to_group(self, iam_service, group_name, policy):
        if group_name in iam_service.groups:
            iam_service.groups[group_name]['policies'].append(policy)
            print(f"Policy assigned to group '{group_name}'.")
    
    def assign_json_policy_to_user(self, iam_service, user_name, policy_json):
        if user_name in iam_service.users:
            iam_service.users[user_name]['policies'].append(policy_json)
            print(f"JSON policy assigned to user '{user_name}'.")
            
    #Método para habilitar MFA para un usuario
    def enable_mfa_for_user(self, iam_service, user_name):
        if user_name in iam_service.users:
            iam_service.users[user_name]['mfa_enabled'] = True
            print(f"MFA enabled for user '{user_name}'.")
        else:
            print("Usuario no encontrado")

    #Método para deshabilitar MFA para un usuario
    def deactivate_mfa_for_user(self, iam_service, user_name):
        if user_name in iam_service.users:
            iam_service.users[user_name]['mfa_enabled'] = False
            print(f"MFA deactivated for user '{user_name}'.")
        else:
            print("Usuario no encontrado")

    def list_users(iam_service):
        return list(iam_service.users.keys())
    
    def list_groups(iam_service):
        return list(iam_service.groups.keys())

    def list_policies(iam_service):
        return list(iam_service.policies.name)
    
class Policy:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions


#Crear políticas
admin_policy = Policy("AdminPolicy", ["s3:ListBucket", "ec2:StartInstances"])
group_admin_policy = Policy("GroupAdminPolicy", ["s3:*", "ec2:*"])
read_only_policy = Policy("ReadOnlyPolicy", ["s3:GetObject"])
write_policy = Policy("WritePolicy", ["s3:PutObject"])

iam_service = IAMService()
iam_service.create_user(iam_service, "alice")
iam_service.create_group(iam_service, "admin-group")   
 
print("Users:", iam_service.list_users(iam_service))
print("Groups:", iam_service.list_groups(iam_service))

iam_service.add_user_to_group(iam_service, "alice", "admin-group")

iam_service.policies["ReadOnlyPolicy"] = read_only_policy
iam_service.policies["WritePolicy"] = write_policy
print("Politicas:", iam_service.list_policies(iam_service))

#Agregar políticas por nombre
#iam_service.assign_policy_to_user(iam_service, "alice", "AdminPolicy")
#iam_service.assign_policy_to_group(iam_service, "admin-group", "GroupAdminPolicy")

#Agregar políticas
iam_service.assign_policy_to_user(iam_service, "alice", read_only_policy)
iam_service.assign_policy_to_group(iam_service, "admin-group", write_policy)

# Agregar políticas al IAM
iam_service.policies["AdminPolicy"] = admin_policy
iam_service.policies["GroupAdminPolicy"] = group_admin_policy

#Asignar políticas a usuario
iam_service.assign_policy_to_user(iam_service, "alice", admin_policy)

#Asignar políticas a grupo
iam_service.assign_policy_to_group(iam_service, "admin-group", group_admin_policy)

# MFA
iam_service.enable_mfa_for_user(iam_service, "alice")
setup_mfa("alice")

#Política de contraseña
set_password_policy(8, True, True)

# Políticas JSON
politica_json1=crear_json_policy()
iam_service.assign_json_policy_to_user(iam_service, "alice", politica_json1)