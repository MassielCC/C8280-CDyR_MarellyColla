import os
import heapq
import random
import time
import logging

# Crear la carpeta "Registros" si no existe
if not os.path.exists('Registros'):
    os.makedirs('Registros')

# Configurar logging para guardar registros en un archivo
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', filename='Registros/logfile.log', filemode='w')

class NotificationSystem:
    def __init__(self):
        self.topics = {}
        self.retry_limit = 3

    def create_topic(self, name):
        self.topics[name] = []
        logging.info(f"Tema creado: {name}")

    def subscribe(self, topic, endpoint):
        if topic in self.topics:
            self.topics[topic].append(endpoint)
            if isinstance(endpoint.name, SQSQueue):
                logging.info(f"Suscripcion agregada: {endpoint.name.name_queue} al tema {topic}")
            else:
                logging.info(f"Suscripcion agregada: {endpoint.name} al tema {topic}")
        else:
            raise Exception("El tema no existe")

    def unsubscribe(self, topic, endpoint):
        if topic in self.topics:
            self.topics[topic].remove(endpoint)
            if isinstance(endpoint.name, SQSQueue):
                logging.info(f"Suscripcion eliminada: {endpoint.name.name_queue} al tema {topic}")
            else:
                logging.info(f"Suscripcion eliminada: {endpoint.name} del tema {topic}")
        else:
            raise Exception("El tema no existe")

    def publish(self, topic, message, priority=0):
        if topic in self.topics:
            for endpoint in self.topics[topic]:
                heapq.heappush(endpoint.message_queue, (priority, message))
                logging.info(f"Mensaje publicado en tema {topic}: {message} con PRIORIDAD-{priority}")
                time.sleep(1)
                self.send_notifications(endpoint, topic)
        else:
            raise Exception("El tema no existe")

    def send_notifications(self, endpoint, topic):
        while endpoint.message_queue:
            priority, message = heapq.heappop(endpoint.message_queue)
            success = self.attempt_send(endpoint, message)
            if success and isinstance(endpoint.name, SQSQueue):
                endpoint.name.send_message_SNS(message, topic, priority)
            if not success:
                self.retry(endpoint, message, priority)

    def attempt_send(self, endpoint, message):
        if endpoint.notify(message):
            if isinstance(endpoint.name, SQSQueue):
                logging.info(f"Notificacion enviada con exito a {endpoint.name.name_queue}: {message}")
            else:
                logging.info(f"Notificacion enviada con exito a {endpoint.name}: {message}")
            time.sleep(1)
            return True
        else:
            if isinstance(endpoint.name, SQSQueue):
                logging.info(f"Fallo al enviar notificacion a {endpoint.name.name_queue}: {message}")
            else:
                logging.info(f"Fallo al enviar notificacion a {endpoint.name}: {message}")
            time.sleep(1)
            return False

    def retry(self, endpoint, message, priority):
        attempts = 1
        while attempts <= self.retry_limit:
            if isinstance(endpoint.name, SQSQueue):
                logging.info(f"Reintentando ({attempts}/{self.retry_limit}) para {endpoint.name.name_queue}")
            else:
                logging.info(f"Reintentando ({attempts}/{self.retry_limit}) para {endpoint.name}")
            time.sleep(1)
            if self.attempt_send(endpoint, message):
                return True
            attempts += 1
        if isinstance(endpoint.name, SQSQueue):
            logging.info(f"Notificacion fallida despues de {self.retry_limit} intentos para {endpoint.name.name_queue}")
        else:
            logging.info(f"Notificacion fallida despues de {self.retry_limit} intentos para {endpoint.name}")

class Endpoint:
    def __init__(self, protocolo, name):
        self.protocolo = protocolo
        self.name = name
        self.message_queue = []

    def notify(self, message):
        if random.random() > 0.7:
            return False
        return True

class SQSQueue:
    def __init__(self, name_queue):
        self.name_queue = name_queue
        self.queue = []
        self.dql = []
        self.retry_limit = 3

    def send_message_SNS(self, message, topic, priority=0):
        heapq.heappush(self.queue, (priority, topic, message))
        logging.info(f"Mensaje de {topic} agregado a la cola")

    def verify_message_queue(self):
        if self.queue:
            logging.info("Obteniendo el mensaje de mayor prioridad ...")
            return heapq.nsmallest(1, self.queue)[0]
        else:
            logging.info("No hay mensajes en la cola")
            return None

    def process_message(self):
        while True:
            item_mensaje = self.verify_message_queue()
            if not item_mensaje:
                break
            prioridad, topico, mensaje = item_mensaje
            attempt = 0
            try:
                while attempt < self.retry_limit:
                    if random.choice([True, False]):
                        logging.info(f"Mensaje procesado {mensaje} de {topico}")
                        heapq.heappop(self.queue)
                        break
                    else:
                        attempt += 1
                        logging.warning(f"Fallo al procesar el mensaje: {mensaje} de {topico}. Intento {attempt}")

                if attempt >= 3:
                    heapq.heappush(self.dql, (prioridad, topico, mensaje))
                    logging.info(f"Agregando {topico}: {mensaje} a la cola de mensajes muertos")
            except Exception as e:
                logging.error(f"Error al procesar el mensaje: {e}")

# Ejemplo de uso
sns = NotificationSystem()
email_endpoint = Endpoint("email", "alumno.cayetano@upch.pe")
sms_endpoint = Endpoint("sms", "+123456789")
sqs = SQSQueue("COLA-01")
sqs_endpoint = Endpoint("sqs", sqs)

sns.create_topic("ALERTAS CAYETANO")
sns.subscribe("ALERTAS CAYETANO", email_endpoint)
sns.subscribe("ALERTAS CAYETANO", sms_endpoint)
sns.subscribe("ALERTAS CAYETANO", sqs_endpoint)

sns.publish("ALERTAS CAYETANO", "Mensaje de alta prioridad", priority=1)
time.sleep(2)

sns.create_topic("NOVEDADES CAYETANO")
sns.subscribe("NOVEDADES CAYETANO", sqs_endpoint)
sns.publish("NOVEDADES CAYETANO", "Mensaje de prioridad media", priority=2)
sns.publish("NOVEDADES CAYETANO", "Mensaje de baja prioridad", priority=3)

sns.create_topic("ACTUALIZACIONES CAYETANO")
sns.subscribe("ACTUALIZACIONES CAYETANO", sqs_endpoint)
sns.publish("ACTUALIZACIONES CAYETANO", "Mensaje de prioridad media", priority=2)
time.sleep(2)

print(f"Mensajes en {sqs.name_queue}: {sqs.queue}")
sqs.process_message()
