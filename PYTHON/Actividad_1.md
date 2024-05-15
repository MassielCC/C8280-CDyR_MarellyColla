## Problema 1: Simulación de un cliente-servidor
Conceptos: Cliente, Servidor, Protocolo, TCP/IP

Escribe una función en Python que simule la comunicación entre un cliente y un servidor usando la programación funcional. El cliente debería ser capaz de enviar mensajes y el servidor de responder de acuerdo con un protocolo simple (por ejemplo, eco, reverso del mensaje, etc.).

* Implementa funciones separadas para el comportamiento del cliente y del servidor.
* Simula el envío y recepción de mensajes.
* Aplica conceptos de TCP/IP en un contexto abstracto.

## SOLUCIÓN
``` Python
# Definir las funciones del servidor
def servidor(mensaje):
    """Procesa los mensajes enviados por el cliente según el comando especificado."""
    comando, _, contenido = mensaje.partition(':')
    if comando.strip().lower() == 'eco':
        return contenido.strip()
    elif comando.strip().lower() == 'reverso':
        return contenido.strip()[::-1]
    else:
        return "Comando no reconocido."

# Definir el cliente
def cliente(mensaje):
    """Envía mensajes al servidor y procesa la respuesta."""
    respuesta = servidor(mensaje)
    print(f"Servidor dice: {respuesta}")

def main():
    cliente("eco: Hola Mundo")
    cliente("reverso: Hola Mundo")
    cliente("sumar: 123 + 456")  # Este debería dar un error ya que no está implementado

if __name__ == "__main__":
    main()

```

## Ejercicios para extender la simulación
* Agregar más comandos: Implementa más funcionalidades en el servidor, como sumar números o convertir el mensaje a mayúsculas. 
* Validación de mensajes: Agrega validaciones para asegurarte de que los mensajes sigan el formato correcto antes de procesarlos. 
Formato-->  comando: mensaje
Se incluyo validación de estructura y mensaje vacio
* Simular retrasos de Red: Introduce retrasos aleatorios para simular la latencia de la red y observa cómo afecta la comunicación.
Uso de time.sleep() para generar el retraso y random para que el tiempo sea aleatorio. 