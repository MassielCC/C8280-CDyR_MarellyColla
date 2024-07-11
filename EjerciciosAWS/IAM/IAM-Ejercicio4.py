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

    #Método para mostrar los cambios
    def mostrar(self, iam_service):
        for user in iam_service.users:
            print(f"User {user} , {iam_service.users[user]['mfa_enabled']}" )
            

iam_service = IAMService()
iam_service.create_user(iam_service, "alice")
iam_service.create_user(iam_service, "massiel")
iam_service.enable_mfa_for_user(iam_service, "alice")
iam_service.mostrar(iam_service)

iam_service.deactivate_mfa_for_user(iam_service, "alicia")
iam_service.mostrar(iam_service)
