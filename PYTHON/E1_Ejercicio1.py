import random
import time

# Definimos la clase Servidor
class Servidor:
    def __init__(self):
        self.estado = "LISTENING"

    def recibir_syn(self):
        if random.choice([True, False]):  # Simulamos la pérdida de paquetes
            print("Servidor: Paquete SYN recibido.")
            self.estado = "SYN_RECEIVED"
            return True
        else:
            print("Servidor: Paquete SYN perdido.")
            return False

    def enviar_syn_ack(self):
        if random.choice([True, False]):  # Simulamos la pérdida de paquetes
            print("Servidor: Enviando SYN-ACK.")
            return True
        else:
            print("Servidor: Paquete SYN-ACK perdido.")
            return False

    def recibir_ack(self):
        if random.choice([True, False]):  # Simulamos la pérdida de paquetes
            print("Servidor: Paquete ACK recibido.")
            self.estado = "ESTABLISHED"
            return True
        else:
            print("Servidor: Paquete ACK perdido.")
            return False

# Definimos la clase Cliente
class Cliente:
    def __init__(self):
        self.estado = "CLOSED"

    def enviar_syn(self, servidor):
        print("Cliente: Enviando SYN.")
        if servidor.recibir_syn():
            self.estado = "SYN_SENT"
            return True
        else:
            print("Cliente: Reintentando enviar SYN.")
            return False

    def recibir_syn_ack(self, servidor):
        if servidor.enviar_syn_ack():
            print("Cliente: Paquete SYN-ACK recibido.")
            self.estado = "SYN_RECEIVED"
            return True
        else:
            print("Cliente: Esperando SYN-ACK.")
            return False

    def enviar_ack(self, servidor):
        print("Cliente: Enviando ACK.")
        if servidor.recibir_ack():
            self.estado = "ESTABLISHED"
            print("Cliente: Conexión establecida.")
            return True
        else:
            print("Cliente: Reintentando enviar ACK.")
            return False


# Función para simular el proceso de three-way handshake
def three_way_handshake(cliente, servidor):
    while not cliente.enviar_syn(servidor):
        time.sleep(1)

    while not cliente.recibir_syn_ack(servidor):
        time.sleep(1)

    while not cliente.enviar_ack(servidor):
        time.sleep(1)

# Crear instancias de Cliente y Servidor
cliente = Cliente()
servidor = Servidor()

# Simular el three-way handshake
three_way_handshake(cliente, servidor)

# Función extendida para manejar múltiples clientes
def multiple_client_handshake(clientes, servidor):
    for cliente in clientes:
        print(f"Iniciando handshake para el Cliente {clientes.index(cliente) + 1}")
        three_way_handshake(cliente, servidor)
        print("")

# Crear múltiples instancias de Cliente
clientes = [Cliente() for _ in range(3)]

# Simular el three-way handshake para múltiples clientes
multiple_client_handshake(clientes, servidor)