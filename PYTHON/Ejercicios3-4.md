## Problema 3: Encriptación y desencriptación
Conceptos: Encriptación y desencriptación, clave Pública, clave Privada

Escribe funciones para encriptar y desencriptar mensajes usando un enfoque funcional. Usa un método simple de encriptación como el cifrado César para ilustrar cómo se podrían manejar las llaves.

Crea funciones para encriptar y desencriptar mensajes.
Simula el uso de llaves públicas y privadas en la encriptación/desencriptación.

# Respuesta 3
Para este problema, implementaremos un método simple de encriptación y desencriptación utilizando el cifrado César, que es un tipo de cifrado por sustitución donde cada letra en el texto original es desplazada un cierto número de lugares hacia abajo o hacia arriba en el alfabeto. Aunque este método es bastante básico y no utiliza directamente claves pública y privada como en los sistemas criptográficos modernos, podemos adaptarlo para simular el concepto usando "claves" que determinan el desplazamiento.

## Paso 1: Crea las funciones de encriptación y desencriptación

Primero, definiremos las funciones de encriptación y desencriptación. Para mantenerlo simple y funcional, consideraremos sólo letras del alfabeto inglés y omitiremos otros caracteres.

```Python
def cifrado_cesar(texto, desplazamiento):
    """Encripta el texto utilizando el cifrado César con un desplazamiento dado."""
    resultado = ""
    for char in texto:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            resultado += chr((ord(char) - offset + desplazamiento) % 26 + offset)
        else:
            resultado += char
    return resultado

def descifrado_cesar(texto_cifrado, desplazamiento):
    """Desencripta el texto cifrado utilizando el cifrado César con el desplazamiento dado."""
    return cifrado_cesar(texto_cifrado, -desplazamiento)

```
## Paso 2: Simular el uso de claves públicas y privadas
En el cifrado César, el "desplazamiento" actúa como una clave. Para simular un sistema de clave pública y clave privada:

Podríamos definir que la "clave pública" es el desplazamiento usado para cifrar. La "clave privada" sería el desplazamiento negativo (o el desplazamiento complementario hasta 26) necesario para descifrar. Esto no es realmente un uso de claves pública/privada como en criptografía RSA, pero ayuda a ilustrar el concepto de que una clave es conocida por todos (pública) y la otra es mantenida en secreto (privada).

```Python
def demostracion():
    mensaje_original = "Hola Mundo"
    desplazamiento = 4  # Esta sería la "clave pública"

    mensaje_cifrado = cifrado_cesar(mensaje_original, desplazamiento)
    print("Mensaje cifrado:", mensaje_cifrado)

    mensaje_descifrado = descifrado_cesar(mensaje_cifrado, desplazamiento)
    print("Mensaje descifrado:", mensaje_descifrado)

if __name__ == "__main__":
    demostracion()
```

# Ejercicios adicionales para extender el uso
- Amplía las funciones para que trabajen con todos los caracteres ASCII imprimibles, no sólo las letras.

# 1:
```Python
def cifrado_cesar(texto, desplazamiento):
    """Encripta el texto utilizando el cifrado César con un desplazamiento dado."""
    resultado = ""
    for char in texto:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            resultado += chr((ord(char) - offset + desplazamiento) % 26 + offset)
        else:
            if char == " ":
                resultado+=char
            else:
                resultado += chr(ord(char) + desplazamiento)
    return resultado
```

---

- Considera explorar algoritmos como RSA para un ejemplo real de uso de criptografía con clave pública y privada.

**Algoritmo RSA**
Trabaja con una llave pública y privada


---

- Analiza la seguridad del cifrado César y cómo se podría mejorar usando una técnica más compleja, como el cifrado Vigenère.

**Cifrado Vigenere**: es más complejo que el cifrado César, usa diferentes desplazamientos para cada letra basado en una palabra que le proporcionamos. En el caso de este cifrado la palabra dada sería nuestra llave pública.

![Cifrado Vigenere](https://edea.juntadeandalucia.es/bancorecursos/file/861144ef-7413-4512-9eea-7fe25098db20/1/CDI_1BAC_REA02_V01.zip/Cuadro_Vigenere.png)

El cifrado César es fácil de entender ya que el desplazamiento es el mismo para cada letra, es suficiente que descifremos el desplazamiento de 1 letra y ya tenemos todo la frase descifrada. Sin embargo con el cifrado Vigenere hay 1 desplazamiento diferente por cada letra, lo que supone una mejora en la seguridad de la encriptación de nuestro mensaje. 

---

## Problema 4: Simulación del modelo OSI
Conceptos: Modelo OSI, Encapsulación de Datos, Protocol Stack

Desarrolla una serie de funciones que simulan la transmisión de datos a través de las diferentes capas del modelo OSI, mostrando cómo se encapsulan y desencapsulan los datos en cada capa.

Implementa funciones que representen cada capa del modelo OSI.
Simula el proceso de encapsulación y desencapsulación de datos.

## Ejercicios adicionales para extender el uso
- Implementa un mecanismo para manejar errores en cada capa.
- Simula más detalles de cada capa, por ejemplo, manejar la segmentación en la capa de transporte o las direcciones IP en la capa de red.
- Utiliza estas funciones en combinación con sockets para enviar y recibir datos a través de una red real, manteniendo la simulación de encapsulación y desencapsulación.