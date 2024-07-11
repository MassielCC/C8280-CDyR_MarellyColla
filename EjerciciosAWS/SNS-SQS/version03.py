# Versión 3: Implementación con reintentos
# Mejora con reintentos automáticos en caso de fallos en el envío de notificaciones

import heapq  # Para usar una cola de prioridad
import random  # Para simular fallos aleatorios

class NotificationSystem: # Clase para gestionar temas y suscripciones con soporte para prioridades y reintentos.
    def __init__(self):
        self.topics = {}  # Diccionario para almacenar los temas y sus suscripciones
        self.retry_limit = 3  # Límite máximo de reintentos

    def create_topic(self, name):
        self.topics[name] = []  # Crea un nuevo tema con el nombre especificado
        print(f"Tema creado: {name}")  # Registro de creación de tema
        return name

    def subscribe(self, topic, endpoint): # Suscribe un endpoint al tema especificado
        if topic in self.topics:
            self.topics[topic].append(endpoint)
            print(f"Suscripción añadida: {endpoint.name} al tema {topic}")  # Registra la suscripción del endpoint
        else:
            raise Exception("El tema no existe")  # Levanta una excepción si el tema no existe

    def unsubscribe(self, topic, endpoint): # Desuscribe un endpoint del tema especificado
        if topic in self.topics:
            self.topics[topic].remove(endpoint)
            print(f"Suscripción eliminada: {endpoint.name} del tema {topic}")  # Registra la desuscripción del endpoint
        else:
            raise Exception("El tema no existe")  # Levanta una excepción si el tema no existe

    def publish(self, topic, message, priority=0): # Publica un mensaje en el tema especificado con una prioridad opcional.
        if topic in self.topics:
            for endpoint in self.topics[topic]:
                heapq.heappush(endpoint.message_queue, (priority, message))
                print(f"Mensaje publicado en tema {topic}: {message} con prioridad {priority}")  # Registra la publicación del mensaje en el tema con prioridad
                self._send_notifications(endpoint)  # Intentar enviar las notificaciones
        else:
            raise Exception("El tema no existe")  # Levanta una excepción si el tema no existe

    def _send_notifications(self, endpoint): # Envía notificaciones desde la cola de prioridad al endpoint especificado
        while endpoint.message_queue:
            priority, message = heapq.heappop(endpoint.message_queue)
            success = self._attempt_send(endpoint, message)
            if not success:
                self._retry(endpoint, message, priority) #  reintentos en caso de fallos y registra eventos de reintentos.

    def _attempt_send(self, endpoint, message): # Intenta enviar un mensaje al endpoint especificado
        if endpoint.notify(message):
            print(f"Notificación enviada con éxito a {endpoint.name}: {message}")  # Registro de éxito en envío de notificación
            return True
        else:
            print(f"Fallo al enviar notificación a {endpoint.name}: {message}")  # Registro de fallo en envío de notificación
            return False

    def _retry(self, endpoint, message, priority): # Reintenta enviar un mensaje fallido al endpoint especificado.
        attempts = 1
        while attempts <= self.retry_limit: # Realiza múltiples intentos hasta alcanzar el límite máximo de reintentos
            print(f"Reintentando ({attempts}/{self.retry_limit}) para {endpoint.name}")  # Registro de intento de reenvío
            if self._attempt_send(endpoint, message):
                return
            attempts += 1
        print(f"Notificación fallida después de {self.retry_limit} intentos para {endpoint.name}")  # Registro de fallo tras reintentos

class Endpoint: # Clase que representa un punto de entrega de notificaciones con cola de prioridad y simulación de fallos
    def __init__(self, name):
        self.name = name
        self.message_queue = []  # Cola de prioridad para los mensajes

    def notify(self, message): # Envía una notificación al endpoint con una simulación de fallo aleatorio.
        if random.random() > 0.3:  # Simular fallos aleatorios con una probabilidad del 30%
            return False
        return True # Retorna True si la notificación se envió correctamente

# Ejemplo de uso
sns = NotificationSystem()
email_endpoint = Endpoint("usuario@example.com")
sms_endpoint = Endpoint("+123456789")

sns.create_topic("alertas")
sns.subscribe("alertas", email_endpoint)
sns.subscribe("alertas", sms_endpoint)

sns.publish("alertas", "Este es un mensaje de alerta", priority=1)
