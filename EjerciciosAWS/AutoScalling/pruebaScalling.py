class AutoScalingGroup:
    def __init__(self, template, min_size, max_size):
        self.template = template # Inicializa la plantilla de servidor
        self.min_size = min_size # Tamaño mínimo del grupo de servidores
        self.max_size = max_size # Tamaño máximo del grupo de servidores
        self.servers = self.configurar_plantilla_lanzamiento() # Crea los servidores iniciales según el tamaño mínimo
        self.cpu_upper_threshold = 70 # Límite superior
        self.cpu_lower_threshold = 30 # Límite inferior

    def configurar_plantilla_lanzamiento(self):
        print("1: Configurar manualmente, 2: Configuración por default")
        op=int(input("Elegir una opción: "))
        if op == 1:
            name=input("Ingresar el nombre: ")
            description= input("Ingresar la descripción: ")
            ami=self.template.elegir_ami()
            return [self.template.create_server(name, description, ami) for _ in range(self.min_size)]
        elif op==2:
            return [self.template.create_server() for _ in range(self.min_size)]
        else:
            print("Opción inválida")
            return [self.template.create_server() for _ in range(self.min_size)]
            
    def mostrar_servers(self):
        for i in range(len(self.servers)):
            print(f"{i}: {self.servers[i]}")
            
    def scale_out(self): 
        if len(self.servers) < self.max_size:
            self.servers.append(self.template.create_server()) # Añade un servidor si no se ha alcanzado el tamaño máximo
            print("Scaled out: Added a server. Total servers:", len(self.servers))
    
    def scale_in(self):
        if len(self.servers) > self.min_size:
            self.servers.pop() # Elimina un servidor si no se ha alcanzado el tamaño mínimo
            print("Scaled in: Removed a server. Total servers:", len(self.servers))

    def politica_escalado(self, nuevo_minimo_cpu, nuevo_maximo_cpu):
        self.min_size = nuevo_minimo_cpu
        self.max_size = nuevo_maximo_cpu

    def adjust_capacity(self, cpu_usages):
        average_cpu_usage = sum(cpu_usages)/len(cpu_usages) # Calcula el uso promedio de CPU
        if average_cpu_usage > self.cpu_upper_threshold:
            self.scale_out() # Escala hacia afuera si el uso de CPU supera el limite
        elif average_cpu_usage < self.cpu_lower_threshold:
            self.scale_in() # Escala hacia adentro si el uso de CPU está por debajo del limite

class ServerTemplate:
    def create_server(self, name, description, ami):
        # Crea y devuelve un nuevo servidor
        return Server(nombre=name, description=description, AMI=ami)
    def elegir_ami(self):
        opciones= {1:"Linux", 2:"macOS", 3:"Ubuntu", 4:"Windows", 5:"Red Hat", 6:"Debian"}
        print("Opciones: ", opciones)
        elegido=int(input("Elige una opción: "))
        if opciones.get(elegido) != None:
             return opciones[elegido]
        else:
            print("Opción inválida")
            return "Linux"
            
class Server:
    def __init__(self, nombre="my_template", description="Plantilla", AMI="Linux",tipo_instancia="t2.micro", grupo_seguridad="EC2GroupSecurity"):
        self.nombre= nombre
        self.description=description
        self.AMI=AMI
        self.tipo_instancia=tipo_instancia
        self.grupo_seguridad=grupo_seguridad

    def __str__(self):
        return f"Server(nombre={self.nombre}, AMI ={self.AMI}, tipo_instancia={self.tipo_instancia}, grupo_seguridad={self.grupo_seguridad})"

#casos de uso
template1=ServerTemplate()
asg=AutoScalingGroup(template=template1, min_size=2, max_size=5)
asg.adjust_capacity([60,80,70])
print("Mostrar servidores:")
asg.mostrar_servers()
