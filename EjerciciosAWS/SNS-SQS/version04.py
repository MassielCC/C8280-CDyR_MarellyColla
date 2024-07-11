# Versión 4: Implementación con registro de logs
# Mejora con registro de logs de los eventos de envío y recepción de notificaciones

import heapq  # Para usar una cola de prioridad
import random  # Para simular fallos aleatorios
import time  # Para obtener timestamps locales y pausas

class NotificationSystem:  # Clase para gestionar temas y suscripciones con soporte para prioridades, reintentos y registro de logs
    def __init__(self):
        self.topics = {}  # Diccionario para almacenar los temas y sus suscripciones
        self.retry_limit = 3  # Límite máximo de reintentos
        self.log = []  # Lista para almacenar los registros de logs

    def create_topic(self, name):  # Crea un nuevo tema con el nombre especificado
        self.topics[name] = []  # Inicializa el tema con una lista vacía de suscripciones
        self.add_log(f"Tema creado: {name}")  # Registro de creación de tema en el log
        return name

    def subscribe(self, topic, endpoint):  # Suscribe un endpoint al tema especificado
        if topic in self.topics:
            self.topics[topic].append(endpoint)
            self.add_log(f"Suscripción añadida: {endpoint.name} al tema {topic}")  # Registro de suscripción del endpoint en el log
        else:
            raise Exception("El tema no existe")  # Levanta una excepción si el tema no existe

    def unsubscribe(self, topic, endpoint):  # Desuscribe un endpoint del tema especificado
        if topic in self.topics:
            self.topics[topic].remove(endpoint)
            self.add_log(f"Suscripción eliminada: {endpoint.name} del tema {topic}")  # Registro de desuscripción del endpoint en el log
        else:
            raise Exception("El tema no existe")  # Levanta una excepción si el tema no existe

    def publish(self, topic, message, priority=0):  # Publica un mensaje en el tema especificado con una prioridad opcional
        if topic in self.topics:
            for endpoint in self.topics[topic]:
                heapq.heappush(endpoint.message_queue, (priority, message))
                self.add_log(f"Mensaje publicado en tema {topic}: {message} con prioridad {priority}")  # Registro de publicación del mensaje con prioridad en el log
                time.sleep(1)  # Pausa de 1 segundo para simular el tiempo de procesamiento
                self._send_notifications(endpoint)  # Intentar enviar las notificaciones
                print("\n")  # Agregar un salto de línea entre bloques de mensajes
        else:
            raise Exception("El tema no existe")  # Levanta una excepción si el tema no existe

    def _send_notifications(self, endpoint):  # Envía notificaciones desde la cola de prioridad al endpoint especificado
        while endpoint.message_queue:  # Maneja reintentos en caso de fallos y registra eventos de reintentos en el log
            priority, message = heapq.heappop(endpoint.message_queue)
            success = self._attempt_send(endpoint, message)
            if not success:
                self._retry(endpoint, message, priority)

    def _attempt_send(self, endpoint, message):  # Intenta enviar un mensaje al endpoint especificado
        if endpoint.notify(message):
            self.add_log(f"Notificación enviada con éxito a {endpoint.name}: {message}")  # Registro de éxito en envío de notificación en el log
            time.sleep(1)  # Pausa de 1 segundo para simular el tiempo de procesamiento
            return True
        else:
            self.add_log(f"Fallo al enviar notificación a {endpoint.name}: {message}")  # Registro de fallo en envío de notificación en el log
            time.sleep(1)  # Pausa de 1 segundo para simular el tiempo de procesamiento
            return False

    def _retry(self, endpoint, message, priority):  # Reintenta enviar un mensaje fallido al endpoint especificado
        attempts = 1
        while attempts <= self.retry_limit:  # Realiza múltiples intentos hasta alcanzar el límite máximo de reintentos
            self.add_log(f"Reintentando ({attempts}/{self.retry_limit}) para {endpoint.name}")  # Registro de intento de reenvío en el log
            time.sleep(1)  # Pausa de 1 segundo para simular el tiempo de procesamiento
            if self._attempt_send(endpoint, message):
                return
            attempts += 1
        self.add_log(f"Notificación fallida después de {self.retry_limit} intentos para {endpoint.name}")  # Registro de fallo tras reintentos en el log

    def add_log(self, message):  # Añade un evento al registro de logs con un timestamp local
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # Obtiene la hora actual en formato local
        log_entry = f"{timestamp} - {message}"
        self.log.append(log_entry)  # Añade el mensaje al registro de logs
        print(log_entry)  # Imprime el registro de log con timestamp local

class Endpoint:  # Clase que representa un punto de entrega de notificaciones con cola de prioridad, simulación de fallos y logging
    def __init__(self, name):
        self.name = name
        self.message_queue = []  # Cola de prioridad para los mensajes

    def notify(self, message):  # Envía una notificación al endpoint con una simulación de fallo aleatorio
        if random.random() > 0.3:  # Simular fallos aleatorios con una probabilidad del 30%
            return False
        return True  # Retorna True si la notificación se envió correctamente

# Ejemplo de uso
sns = NotificationSystem()
email_endpoint = Endpoint("edwin.jara@upch.pe")
sms_endpoint = Endpoint("+123456789")

# Crear tema y suscribir endpoints
sns.create_topic("alertas")
sns.subscribe("alertas", email_endpoint)
sns.subscribe("alertas", sms_endpoint)

# Publicar mensajes con diferentes prioridades
sns.publish("alertas", "Mensaje de alta prioridad", priority=1)
time.sleep(2)

sns.publish("alertas", "Mensaje de baja prioridad", priority=3)
time.sleep(2)

sns.publish("alertas", "Mensaje de prioridad media", priority=2)
time.sleep(2)

# Publicar más mensajes para ver reintentos y logs
sns.publish("alertas", "Otro mensaje de alta prioridad", priority=1)
time.sleep(2)

sns.publish("alertas", "Otro mensaje de baja prioridad", priority=3)
time.sleep(2)

# Desuscribir un endpoint y publicar un mensaje
sns.unsubscribe("alertas", email_endpoint)
sns.publish("alertas", "Mensaje después de desuscribir email", priority=1)
time.sleep(2)