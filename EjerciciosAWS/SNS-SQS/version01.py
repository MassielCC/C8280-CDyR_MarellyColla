# Versión 1: Implementación básica
# Implementación inicial de un sistema de notificaciones con gestión básica de temas y suscripciones

class NotificationSystem: # Clase para gestionar temas y suscripciones básicas
    def __init__(self):
        self.topics = {}  # Diccionario para almacenar los temas y sus suscripciones

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

    def publish(self, topic, message): # Publica un mensaje en el tema especificado
        if topic in self.topics:
            for endpoint in self.topics[topic]:
                endpoint.notify(message)
                print(f"Mensaje publicado en tema {topic}: {message}")  # Registra la publicación del mensaje en el tema
        else:
            raise Exception("El tema no existe")  # Levanta una excepción si el tema no existe

class Endpoint: # Clase que representa un punto de entrega de notificaciones
    def __init__(self, name):
        self.name = name

    def notify(self, message): # Envía una notificación al endpoint
        print(f"Notificación para {self.name}: {message}")  # Registra la notificación enviada al endpoint

# Ejemplo de uso
sns = NotificationSystem()
email_endpoint = Endpoint("usuario@example.com")
sms_endpoint = Endpoint("+123456789")

sns.create_topic("alertas")
sns.subscribe("alertas", email_endpoint)
sns.subscribe("alertas", sms_endpoint)

sns.publish("alertas", "Este es un mensaje de alerta")