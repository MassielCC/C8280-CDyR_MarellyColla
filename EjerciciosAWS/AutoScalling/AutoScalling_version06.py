import time

class CustomAutoScalingGroup:
    def __init__(self, template, min_size, max_size):
        self.template = template  # Plantilla de servidor utilizada para crear nuevos servidores
        self.min_size = min_size  # Tamaño mínimo del grupo de servidores
        self.max_size = max_size  # Tamaño máximo del grupo de servidores
        self.servers = self.configurar_plantilla_lanzamiento()  # Crea los servidores iniciales según la plantilla y tamaño mínimo
        self.memory_threshold = 70  # Umbral de uso de memoria para escalar
        self.log = []  # Lista de logs de eventos
        self.add_log(f"Grupo de Autoescalado personalizado inicializado con {min_size} servidores.")

    def configurar_plantilla_lanzamiento(self): # Configura la plantilla de lanzamiento de servidores según la opción elegida por el usuario.
        print("1: Configurar manualmente, 2: Configuración por default")
        op = int(input("Elegir una opción: "))
        
        if op == 1:
            name = input("Ingresar el nombre: ")
            description = input("Ingresar la descripción: ")
            ami = self.template.elegir_ami()
            return [self.template.create_server(name, description, ami) for _ in range(self.min_size)]
        elif op == 2:
            return [self.template.create_server() for _ in range(self.min_size)]
        else:
            print("Opción inválida, se utilizará la configuración por default.")
            return [self.template.create_server() for _ in range(self.min_size)]

    def set_memory_scaling_policy(self, memory_threshold): # Establece la política de escalado basada en el uso de memoria.
        self.memory_threshold = memory_threshold  # Establece el umbral de uso de memoria para escalar
        self.add_log(f"Política de escalado basada en memoria establecida en {memory_threshold}%")

    def scale_out(self): # Escala hacia afuera (aumenta el número de servidores) si no se ha alcanzado el tamaño máximo.
        if len(self.servers) < self.max_size:
            self.servers.append(self.template.create_server())  # Añade un nuevo servidor a la lista
            self.add_log("Escalado hacia afuera: Se añadió un servidor")

    def scale_in(self): # Escala hacia adentro (reduce el número de servidores) si no se ha alcanzado el tamaño mínimo.
        if len(self.servers) > self.min_size:
            self.servers.pop()  # Elimina un servidor de la lista
            self.add_log("Escalado hacia adentro: Se eliminó un servidor")

    def adjust_capacity(self, memory_usages): # Ajusta la capacidad del grupo basado en el uso promedio de memoria.
        avg_memory_usage = sum(memory_usages) / len(memory_usages)  # Calcula el uso promedio de memoria
        self.add_log(f"Ajustando capacidad: el uso promedio de memoria es {avg_memory_usage}%")

        if avg_memory_usage > self.memory_threshold:
            self.scale_out()  # Escala hacia afuera si el uso promedio de memoria supera el umbral
        elif avg_memory_usage < self.memory_threshold and len(self.servers) > self.min_size:
            self.scale_in()  # Escala hacia adentro si el uso promedio de memoria es menor que el umbral y hay más servidores de los mínimos

    def print_servers_info(self):
        for i, server in enumerate(self.servers):
            print(f"Información del Servidor {i + 1}: {server}")

    def show_servers_content(self):
        for i, server in enumerate(self.servers):
            print(f"Contenido del Servidor {i + 1}: {server}")

    def add_log(self, message): # Añade un evento al registro de logs con un timestamp.
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # Obtiene la hora actual en formato local
        self.log.append(f"{timestamp} - {message}")  # Añade el mensaje al registro de logs
        print(f"{timestamp} - {message}")

class ServerTemplate:
    def create_server(self, name="my_template", description="Plantilla", ami="Linux"): # Crea y devuelve un nuevo servidor con los parámetros especificados.
        return Server(nombre=name, description=description, ami=ami)

    def elegir_ami(self): # Permite al usuario elegir una opción de sistema operativo para el servidor.
        opciones = {1: "Linux", 2: "macOS", 3: "Ubuntu", 4: "Windows", 5: "Red Hat", 6: "Debian"}
        print("Opciones: ", opciones)
        elegido = int(input("Elige una opción: "))
        if elegido in opciones:
            return opciones[elegido]
        else:
            print("Opción inválida, se seleccionará Linux por default.")
            return "Linux"

class Server:
    def __init__(self, nombre="my_template", description="Plantilla", ami="Linux", tipo_instancia="t2.micro", grupo_seguridad="EC2GroupSecurity"):
        self.nombre = nombre
        self.description = description
        self.ami = ami
        self.tipo_instancia = tipo_instancia
        self.grupo_seguridad = grupo_seguridad

    def __str__(self): # Devuelve una representación en cadena del objeto Server.
        return f"Server(nombre={self.nombre}, AMI={self.ami}, tipo_instancia={self.tipo_instancia}, grupo_seguridad={self.grupo_seguridad})"

# Ejemplo de uso
template = ServerTemplate()  # Crea una plantilla de servidor
custom_asg = CustomAutoScalingGroup(template=template, min_size=2, max_size=5)  # Crea un grupo de autoescalado personalizado

# Establecer la política de escalado basada en memoria
custom_asg.set_memory_scaling_policy(memory_threshold=75)

# Simular métricas de uso de memoria
memory_usages = [80, 85, 70]

custom_asg.adjust_capacity(memory_usages)  # Ajusta la capacidad del grupo basado en los usos de memoria proporcionados
custom_asg.print_servers_info()  # Imprime la información de todos los servidores
custom_asg.show_servers_content()  # Muestra el contenido de todos los servidores
