## Problema 2: Verificación de integridad de datos
Conceptos: Checksum, CRC (Cyclic Redundancy Check)

Desarrolla una función que calcule el checksum o CRC de un string de datos. Esta función será utilizada para verificar la integridad de los datos enviados en un "paquete" de un punto a otro en una red.

* Implementar una función que calcule un checksum simple.
* Implementar una función que calcule el CRC.
* Demuestra cómo se podría utilizar para verificar la integridad de los datos en una red.

## SOLUCIÓN
2 funciones en Python. 
- La primera calculará un checksum simple para un string de datos
- La segunda implementará un Cyclic Redundancy Check (CRC) más robusto. 

1. Función para calcular el checksum simple

El checksum simple que desarrollaremos será la suma de los valores ASCII de los caracteres en el string, reducido a un byte (utilizando módulo 256). Este método es sencillo y rápido, aunque no es muy robusto frente a errores complejos.

2. Función para calcular el CRC: El CRC es un método más avanzado para detectar errores en los datos. Utilizaremos un polinomio común para CRC-32, que es ampliamente usado en software de comunicaciones.

3. Demostración del uso para verificar la integridad de los datos: Podemos demostrar cómo estas funciones pueden ser usadas para verificar la integridad de los datos enviados entre dos puntos en una red simulando el envío de un mensaje que incluye su checksum o CRC, y luego verificando ese valor en el punto de recepción.

```Python
#  Funcion 1
def calcular_checksum_simple(datos):
    """Calcula el checksum simple de un string de datos."""
    return sum(ord(c) for c in datos) % 256

# Funcion 2
def calcular_crc(datos):
    """Calcula el CRC-32 de un string de datos."""
    from zlib import crc32
    return crc32(datos.encode()) & 0xffffffff

# Parte 3
def enviar_datos(datos, metodo='checksum'):
    """Simula el envío de datos incluyendo un checksum o CRC."""
    if metodo == 'checksum':
        checksum = calcular_checksum_simple(datos)
        return datos, checksum
    elif metodo == 'crc':
        crc = calcular_crc(datos)
        return datos, crc

def recibir_datos(datos, valor, metodo='checksum'):
    """Verifica la integridad de los datos recibidos utilizando checksum o CRC."""
    if metodo == 'checksum':
        checksum_calculado = calcular_checksum_simple(datos)
        es_valido = checksum_calculado == valor
    elif metodo == 'crc':
        crc_calculado = calcular_crc(datos)
        es_valido = crc_calculado == valor

    return es_valido

# Demostración
datos_enviados, checksum = enviar_datos("Hola Mundo", metodo='checksum')
print("Checksum enviado:", checksum)
es_correcto = recibir_datos(datos_enviados, checksum, metodo='checksum')
print("¿Checksum correcto?", es_correcto)

datos_enviados, crc = enviar_datos("Hola Mundo", metodo='crc')
print("CRC enviado:", crc)
es_correcto = recibir_datos(datos_enviados, crc, metodo='crc')
print("¿CRC correcto?", es_correcto)
```

**Ejercicios adicionales para extender el uso**
- Simula errores en la transmisión: Modifica los datos entre el envío y la recepción para simular errores en la transmisión y verifica si los métodos de checksum y CRC detectan estos errores.
* Implementa otros algoritmos CRC: Prueba con diferentes polinomios CRC para ver cómo varían en efectividad y complejidad.
Se puede hacer con la librería *crcmod*
* Integra en un sistema de comunicación real: Utiliza estas funciones en un socket de red o en una comunicación serial para ver cómo funcionan en escenarios reales.