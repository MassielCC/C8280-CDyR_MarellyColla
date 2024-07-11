# Versión 6: Implementación de SQS con diferentes colas prioridades
# Mejora con registro de logs de los eventos de envío y recepción de notificaciones

import heapq  # Para usar una cola de prioridad
import random  # Para simular fallos aleatorios
import time  # Para obtener timestamps locales y pausas
import logging

# Configurar logging para registrar eventos importantes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

class NotificationSystem:  # Clase para gestionar temas y suscripciones con soporte para prioridades, reintentos y registro de logs
    def __init__(self):
        self.topics = {}  # Diccionario para almacenar los temas y sus suscripciones
        self.retry_limit = 3  # Límite máximo de reintentos
        self.log = []  # Lista para almacenar los registros de logs

    def create_topic(self, name):  # Crea un nuevo tema con el nombre especificado
        self.topics[name] = []  # Inicializa el tema con una lista vacía de suscripciones
        logging.info(f"Tema creado: {name}")  # Registro de creación de tema en el log
        return name

    def subscribe(self, topic, endpoint):  # Suscribe un endpoint al tema especificado
        #Si el endpoint pertenece a nuestra clase Queue
        if topic in self.topics:
            self.topics[topic].append(endpoint)
            if isinstance(endpoint.name, SQSQueue):
                logging.info(f"Suscripción añadida: {endpoint.name.name_queue} al tema {topic}") # Registro de suscripción del endpoint queue en el log
            else:
                logging.info(f"Suscripción añadida: {endpoint.name} al tema {topic}")  # Registro de suscripción del endpoint en el log
        else:
            raise Exception("El tema no existe")  # Levanta una excepción si el tema no existe

    def unsubscribe(self, topic, endpoint):  # Desuscribe un endpoint del tema especificado
        if topic in self.topics:
            self.topics[topic].remove(endpoint)
            if isinstance(endpoint.name, SQSQueue):
                logging.info(f"Suscripción eliminada: {endpoint.name.name_queue} al tema {topic}") # Registro de desuscripción del endpoint queue en el log
            else:
                logging.info(f"Suscripción eliminada: {endpoint.name} del tema {topic}")  # Registro de desuscripción del endpoint en el log
        else:
            raise Exception("El tema no existe")  # Levanta una excepción si el tema no existe

    def publish(self, topic, message, priority=0):  # Publica un mensaje en el tema especificado con una prioridad opcional
        if topic in self.topics:
            for endpoint in self.topics[topic]:
                heapq.heappush(endpoint.message_queue, (priority, message))
                logging.info(f"Mensaje publicado en tema {topic}: {message} con prioridad {priority}")  # Registro de publicación del mensaje con prioridad en el log
                time.sleep(1)  # Pausa de 1 segundo para simular el tiempo de procesamiento
                self.send_notifications(endpoint, topic)  # Intentar enviar las notificaciones
                print("\n")  # Agregar un salto de línea entre bloques de mensajes
        else:
            raise Exception("El tema no existe")  # Levanta una excepción si el tema no existe

    def send_notifications(self, endpoint, topic):  # Envía notificaciones desde la cola de prioridad al endpoint especificado
        while endpoint.message_queue:  # Maneja reintentos en caso de fallos y registra eventos de reintentos en el log
            priority, message = heapq.heappop(endpoint.message_queue)
            success = self.attempt_send(endpoint, message)
            if success and isinstance(endpoint.name, SQSQueue):
                endpoint.name.send_message_SNS(message, topic, priority)
            if not success:
                self.retry(endpoint, message, priority)

    def attempt_send(self, endpoint, message):  # Intenta enviar un mensaje al endpoint especificado
        if endpoint.notify(message):
            if isinstance(endpoint.name, SQSQueue):
                name_endpoint=endpoint.name.name_queue
            else:
                name_endpoint=endpoint.name
            logging.info(f"Notificación enviada con éxito a {name_endpoint}: {message}")  # Registro de éxito en envío de notificación en el log
            time.sleep(1)  # Pausa de 1 segundo para simular el tiempo de procesamiento
            return True
        else:
            if isinstance(endpoint.name, SQSQueue):
                logging.info(f"Fallo al enviar notificación a {endpoint.name.name_queue}: {message}")  # Registro de fallo en envío de notificación en el log
            else:
                logging.info(f"Fallo al enviar notificación a {endpoint.name}: {message}")  # Registro de fallo en envío de notificación en el log
            time.sleep(1)  # Pausa de 1 segundo para simular el tiempo de procesamiento
            return False

    def retry(self, endpoint, message, priority):  # Reintenta enviar un mensaje fallido al endpoint especificado
        attempts = 1
        while attempts <= self.retry_limit:  # Realiza múltiples intentos hasta alcanzar el límite máximo de reintentos
            if isinstance(endpoint.name, SQSQueue):
                logging.info(f"Reintentando ({attempts}/{self.retry_limit}) para {endpoint.name.name_queue}")  # Registro de intento de reenvío en el log
            else:
                logging.info(f"Reintentando ({attempts}/{self.retry_limit}) para {endpoint.name}")  # Registro de intento de reenvío en el log
            time.sleep(1)  # Pausa de 1 segundo para simular el tiempo de procesamiento
            if self.attempt_send(endpoint, message):
                return True
            attempts += 1
        if isinstance(endpoint.name, SQSQueue):
            logging.info(f"Notificación fallida después de {self.retry_limit} intentos para {endpoint.name.name_queue}")  # Registro de fallo tras reintentos en el log
        else:
            logging.info(f"Notificación fallida después de {self.retry_limit} intentos para {endpoint.name}")  # Registro de fallo tras reintentos en el log

class Endpoint:  # Clase que representa un punto de entrega de notificaciones con cola de prioridad, simulación de fallos y logging
    def __init__(self, protocolo, name):
        self.protocolo = protocolo
        self.name = name
        self.message_queue = []  # Cola de prioridad para los mensajes

    def notify(self, message):  # Envía una notificación al endpoint con una simulación de fallo aleatorio
        if random.random() > 0.7:  # Simular fallos aleatorios con una probabilidad del 30%
            return False
        return True  # Retorna True si la notificación se envió correctamente

class SQSQueue:
    def __init__(self, name_queue):
        self.name_queue=name_queue
        self.queue = []
        self.dql =[] # Dead-letter queues 
        self.retry_limit = 3

    # Añade el mensaje a la cola de prioridad
    def send_message_SNS(self, message, topic, priority=0):
        heapq.heappush(self.queue, (priority, topic, message))
        logging.info(f"Mensaje de {topic} agregado a la cola")

    #Verifica si hay mensajes en cola
    def verify_message_queue(self):
        if self.queue:
            print("Obteniendo el mensaje de mayor prioridad ...")
            return heapq.nsmallest(1, self.queue)[0]
        else:
            print("No hay mensajes en la cola")
            return None
    
    def process_message(self):
        while True: 
            item_mensaje=self.verify_message_queue()
            if not item_mensaje: #si no hay mensajes en cola, no hay mensajes que procesar
                break 
            # Mientras tengamos mensajes en cola
            prioridad, topico, mensaje = item_mensaje
            attempt=0
            try:
                while attempt < self.retry_limit:
                    # Simular procesamiento de mensajes
                    if random.choice([True, False]):
                        logging.info(f"Mensaje procesado {mensaje} de {topico}")
                        heapq.heappop(self.queue) # si se proceso el mensaje se elimina de la cola
                        break
                    else:
                        attempt += 1  
                        logging.warning(f"Fallo al procesar el mensaje: {mensaje} de {topico}. Intento {attempt}")

                if attempt>=3:
                    heapq.heappush(self.dql, (prioridad,topico,mensaje))
                    logging.info(f"Agregando {topico}: {mensaje} a la cola de mensajes muertos")
            except Exception as e:
                #Se envia el mensaje a la cola de mensajes fallidos
                logging.error(f"Error al procesar el mensaje")


# Ejemplo de uso
sns = NotificationSystem()
email_endpoint = Endpoint("email","edwin.jara@upch.pe")
sms_endpoint = Endpoint("sms","+123456789")

#Endpoint SQS queue
sqs=SQSQueue("Cola 1")
sqs_endpoint = Endpoint("sqs",sqs)

# Crear tema y suscribir endpoints
sns.create_topic("alertas")
sns.subscribe("alertas", email_endpoint)
sns.subscribe("alertas", sms_endpoint)
sns.subscribe("alertas", sqs_endpoint)

# Publicar mensajes con diferentes prioridades
sns.publish("alertas", "Mensaje de alta prioridad", priority=1)
time.sleep(2)

# SQS suscrito a múltiples tópicos SNS
sns.create_topic("Novedades")
sns.subscribe("Novedades", sqs_endpoint)
sns.publish("Novedades", "Mensaje de prioridad media", priority=2)
sns.publish("Novedades", "Mensaje de baja prioridad", priority=3)

sns.create_topic("Actualizaciones")
sns.subscribe("Actualizaciones", sqs_endpoint)
sns.publish("Actualizaciones", "Mensaje de prioridad media", priority=2)
time.sleep(2)

# Mensajes en la cola SQS
print(f"Mensajes en {sqs.name_queue}: {sqs.queue}")

# Procesar mensajes en cola SQS
sqs.process_message()