# Genera identificadores únicos universales
import uuid
from datetime import datetime
import time

def generate_temporary_credentials():
    access_key = str(uuid.uuid4()) # generación aleatoria
    secret_key = str(uuid.uuid4())
    session_token = str(uuid.uuid4())
    date_creacion= datetime.now()
    print(f"Temporary credentials generated:\nAccess Key: {access_key}\nSecret Key: {secret_key}\nSession Token: {session_token}")
    print(f"Tiempo de session activa: {date_creacion}")
    print(f"Fecha: {date_creacion.day}/{date_creacion.month}/{date_creacion.year}")
    print(f"Hora: {date_creacion.hour}:{date_creacion.minute}:{date_creacion.second}")
    print(f"Fecha y hora formateada: {date_creacion.strftime('%Y-%m-%d %H:%M:%S')}")

generate_temporary_credentials()

# Ejemplo de diferencia de tiempos
print("Ejemplo de tiempos ----------")
inicio=datetime.now()
time.sleep(5)
fin=datetime.now()
diferencia= fin-inicio
print(diferencia.seconds)