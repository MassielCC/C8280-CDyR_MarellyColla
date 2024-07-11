import time

# Tabla ARP estática inicial
arp_table = {
    '192.168.1.1': '00:1A:2B:3C:4D:5E',
    '192.168.1.2': '00:1A:2B:3C:4D:5F',
    '192.168.1.3': '00:1A:2B:3C:4D:60',
}

# Función para mostrar la tabla ARP actual
def print_arp_table():
    print("Tabla ARP:")
    for ip, mac in arp_table.items():
        print(f"IP: {ip} -> MAC: {mac}")
    print()

# Función para buscar una dirección MAC en la tabla ARP
def arp_lookup(ip):
    mac = arp_table.get(ip)
    if mac:
        print(f"Dirección MAC para {ip} es {mac}")
    else:
        print(f"Solicitando ARP para {ip}...")
        simulate_arp_request(ip)

# Simulación de una solicitud ARP
def simulate_arp_request(ip):
    print(f"Enviando solicitud ARP para {ip}...")
    # Supongamos que recibimos una respuesta con una dirección MAC ficticia
    mac = f"00:1A:2B:3C:4D:{ip.split('.')[-1].zfill(2)}"
    print(f"Respuesta ARP recibida: {ip} -> {mac}")
    arp_table[ip] = mac
    print_arp_table()

# Función para agregar una entrada en la tabla ARP
def add_arp_entry(ip, mac):
    print(f"Agregando entrada ARP: {ip} -> {mac}")
    arp_table[ip] = mac
    print_arp_table()

# Función para eliminar una entrada de la tabla ARP
def remove_arp_entry(ip):
    if ip in arp_table:
        print(f"Eliminando entrada ARP para {ip}")
        del arp_table[ip]
        print_arp_table()
    else:
        print(f"No se encontró una entrada ARP para {ip}")

# Función para envejecer y eliminar entradas antiguas
def age_arp_entries():
    print("Envejeciendo entradas ARP...")
    # Para simplificar, eliminamos todas las entradas
    arp_table.clear()
    print_arp_table()

# Ejemplo de ejecución del simulador ARP
if __name__ == "__main__":
    print_arp_table()
    arp_lookup('192.168.1.1')
    arp_lookup('192.168.1.4')
    add_arp_entry('192.168.1.5', '00:1A:2B:3C:4D:61')
    remove_arp_entry('192.168.1.2')
    time.sleep(2)  # Simula el paso del tiempo
    age_arp_entries()
    arp_lookup('192.168.1.3')
    arp_lookup('192.168.1.5')