## Problema 4: Simulación del modelo OSI
Conceptos: Modelo OSI, Encapsulación de Datos, Protocol Stack

Desarrolla una serie de funciones que simulan la transmisión de datos a través de las diferentes capas del modelo OSI, mostrando cómo se encapsulan y desencapsulan los datos en cada capa.

* Implementa funciones que representen cada capa del modelo OSI.
* Simula el proceso de encapsulación y desencapsulación de datos.

## SOLUCIÓN
Para abordar este problema, implementaremos un conjunto de funciones que simulan el proceso de transmisión de datos a través de las diferentes capas del modelo OSI (Open Systems Interconnection). Cada función representará una capa del modelo y demostrará cómo los datos se encapsulan y desencapsulan a medida que pasan de una capa a otra.

El modelo OSI tiene siete capas:

* Capa de aplicación
* Capa de presentación
* Capa de sesión
* Capa de transporte
* Capa de red
* Capa de enlace de datos
* Capa física

*Paso 1: Definir las funciones de cada capa*
Vamos a definir una función para cada capa, que recibirá los datos de la capa superior, añadirá su propia "cabecera" (simulando la encapsulación), y luego pasará los datos a la siguiente capa.

*Paso 2: Simular el proceso de desencapsulación*
Ahora necesitamos un conjunto de funciones para desencapsular los datos, que se activará en el punto de recepción.

```Python
def capa_aplicacion(datos):
    datos_encapsulados = f"APLICACION({datos})"
    print("Aplicación envía:", datos_encapsulados)
    return capa_presentacion(datos_encapsulados)

def capa_presentacion(datos):
    datos_encapsulados = f"PRESENTACION({datos})"
    print("Presentación envía:", datos_encapsulados)
    return capa_sesion(datos_encapsulados)

def capa_sesion(datos):
    datos_encapsulados = f"SESION({datos})"
    print("Sesión envía:", datos_encapsulados)
    return capa_transporte(datos_encapsulados)

def capa_transporte(datos):
    datos_encapsulados = f"TRANSPORTE({datos})"
    print("Transporte envía:", datos_encapsulados)
    return capa_red(datos_encapsulados)

def capa_red(datos):
    datos_encapsulados = f"RED({datos})"
    print("Red envía:", datos_encapsulados)
    return capa_enlace(datos_encapsulados)

def capa_enlace(datos):
    datos_encapsulados = f"ENLACE({datos})"
    print("Enlace envía:", datos_encapsulados)
    return capa_fisica(datos_encapsulados)

def capa_fisica(datos):
    datos_encapsulados = f"FISICA({datos})"
    print("Física envía:", datos_encapsulados)
    return datos_encapsulados

#Desencapsulación
def desencapsular_fisica(datos):
    return datos[7:-1]

def desencapsular_enlace(datos):
    return desencapsular_fisica(datos[6:-1])

def desencapsular_red(datos):
    return desencapsular_enlace(datos[4:-1])

def desencapsular_transporte(datos):
    return desencapsular_red(datos[11:-1])

def desencapsular_sesion(datos):
    return desencapsular_transporte(datos[7:-1])

def desencapsular_presentacion(datos):
    return desencapsular_sesion(datos[14:-1])

def desencapsular_aplicacion(datos):
    return desencapsular_presentacion(datos[11:-1])

#---------------
def demostracion():
    mensaje_original = "Hola Mundo"
    print("Mensaje original:", mensaje_original)
    
    datos_encapsulados = capa_aplicacion(mensaje_original)
    print("Datos encapsulados:", datos_encapsulados)
    
    datos_desencapsulados = desencapsular_aplicacio(datos_encapsulados)
    print("Datos desencapsulados:", datos_desencapsulados)

if __name__ == "__main__":
    demostracion()

```

## Ejercicios adicionales para extender el uso
- Implementa un mecanismo para manejar errores en cada capa.
- Simula más detalles de cada capa, por ejemplo, manejar la segmentación en la capa de transporte o las direcciones IP en la capa de red.
- Utiliza estas funciones en combinación con sockets para enviar y recibir datos a través de una red real, manteniendo la simulación de encapsulación y desencapsulación.
