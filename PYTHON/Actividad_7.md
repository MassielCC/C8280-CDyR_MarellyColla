## Respuesta 7
Para abordar el problema de simular un caché de red simple, desarrollaremos una función que utilice diccionarios para almacenar y recuperar datos. Este tipo de caché puede ser muy útil para mejorar la eficiencia de las aplicaciones al reducir la cantidad de operaciones de red necesarias, especialmente cuando se trata de datos que se solicitan frecuentemente.

**Paso 1: Crear la estructura del caché**
Usaremos un diccionario para simular el caché. Las claves del diccionario serán las solicitudes o identificadores únicos de los datos, y los valores serán los datos almacenados.

**Paso 2: Simular la obtención de datos y almacenarlos en el caché**
Para simular la obtención de datos y su almacenamiento en el caché, crearemos una función que simule una operación de red (como una solicitud a una base de datos o a una API) y almacene el resultado en el caché para usos futuros.

**Paso 3: Demostrar la mejora en eficiencia**
Para demostrar cómo el caché puede mejorar la eficiencia, realizaremos múltiples solicitudes al mismo identificador y observaremos cómo las solicitudes repetidas evitan operaciones de red adicionales.

```Python
cache_de_red = {}

def obtener_datos_desde_cache(identificador):
    """Obtiene datos del caché si están disponibles."""
    if identificador in cache_de_red:
        print(f"Datos obtenidos desde el caché para: {identificador}")
        return cache_de_red[identificador]
    else:
        print(f"No se encontraron datos en el caché para: {identificador}")
        return None
    
def obtener_datos_desde_servidor(identificador):
    """Simula una operación de red para obtener datos."""
    print(f"Obteniendo datos desde el servidor para: {identificador}")
    # Simulamos una operación de red que obtiene datos
    datos = f"Datos para {identificador}"
    cache_de_red[identificador] = datos
    return datos

def obtener_datos(identificador):
    """Intenta obtener datos desde el caché, y si no están disponibles, los obtiene desde el servidor."""
    datos = obtener_datos_desde_cache(identificador)
    if datos is None:
        datos = obtener_datos_desde_servidor(identificador)
    return datos

def demostrar_eficiencia():
    # Primera solicitud: los datos se obtendrán desde el servidor
    print(obtener_datos("12345"))
    
    # Segunda solicitud: los datos se obtendrán desde el caché
    print(obtener_datos("12345"))
    
    # Tercera solicitud: los datos se obtendrán desde el caché
    print(obtener_datos("12345"))

if __name__ == "__main__":
    demostrar_eficiencia()
```

## Ejercicios adicionales
- **Política de expiración:** Implementa una política de expiración para los datos en el caché, donde los datos se eliminan después de un cierto tiempo.
- **Límite de tamaño:** Establece un límite en el número de entradas que puede contener el caché para evitar el uso excesivo de memoria.
- **Caché distribuido:** Explora cómo se podría implementar un caché distribuido que funcione en múltiples nodos o servidores para mejorar la escalabilidad y la redundancia.

Observaciones: Una política de expiración en el contexto de un caché de red se refiere a un conjunto de reglas que determinan cuánto tiempo se deben almacenar los datos en el caché antes de ser eliminados o invalidados. El objetivo principal es asegurarse de que los datos en el caché sigan siendo relevantes y no consuman recursos innecesariamente. Aquí están algunos de los aspectos clave:

1. Expiración basada en el tiempo: La forma más común de política de expiración es la expiración basada en el tiempo, donde cada entrada en el caché tiene una marca de tiempo de cuando fue almacenada y un tiempo de vida útil predeterminado (TTL, por sus siglas en inglés Time To Live). Una vez que el TTL de una entrada ha expirado, la entrada se considera obsoleta y se elimina del caché. Esto es útil para datos que cambian con frecuencia o que deben ser actualizados regularmente.

2. Expiración basada en eventos: Otra política de expiración es la expiración basada en eventos, donde las entradas del caché se invalidan o actualizan en respuesta a ciertos eventos. Por ejemplo, si un usuario actualiza su perfil en una aplicación, el caché que almacena la información de perfil del usuario podría ser invalidado para forzar una actualización desde el servidor principal la próxima vez que se necesite.

3. Expiración basada en LRU (Least Recently Used): En algunos sistemas de caché, se utiliza un algoritmo LRU para eliminar entradas basándose en su uso. Las entradas que no han sido accedidas recientemente son las primeras en ser eliminadas cuando se necesita hacer espacio para nuevos datos. Esto ayuda a asegurar que el caché contenga sólo los datos más relevantes y frecuentemente accesados.

Por ejemplo básico de cómo podrías implementar una política de expiración basada en el tiempo en Python es así:

```Python
import time

cache_de_red = {}

def almacenar_en_cache(identificador, datos, ttl=300):
    """ Almacena datos en el caché con un tiempo de vida útil (TTL). """
    expiracion = time.time() + ttl  # Establece el tiempo de expiración como el tiempo actual más el TTL
    cache_de_red[identificador] = (datos, expiracion)

def obtener_datos_desde_cache(identificador):
    """ Obtiene datos del caché si están disponibles y no han expirado. """
    if identificador in cache_de_red:
        datos, expiracion = cache_de_red[identificador]
        if time.time() < expiracion:
            print(f"Datos obtenidos desde el caché para: {identificador}")
            return datos
        else:
            print(f"Datos en el caché expirados para: {identificador}")
            del cache_de_red[identificador]  # Elimina datos expirados
    return None
```

Un caché distribuido se refiere a un sistema de caché que funciona a través de múltiples nodos de servidor, a menudo en diferentes ubicaciones geográficas. Esta distribución permite que el caché maneje más datos y más solicitudes de los que podría un único servidor o instancia de caché. Es especialmente útil en entornos donde la carga de acceso a los datos es alta y se requiere alta disponibilidad y escalabilidad.

### Características clave de un caché distribuido:

- **Escalabilidad:** Al distribuir el caché a través de varios nodos, el sistema puede manejar un mayor volumen de solicitudes simultáneamente. Esto es crucial para aplicaciones de alto rendimiento que necesitan servir una gran cantidad de usuarios o procesar grandes volúmenes de datos rápidamente.
- **Redundancia y alta disponibilidad:** La distribución del caché entre múltiples nodos también proporciona redundancia. Si un nodo falla, otros pueden tomar su lugar, asegurando que los datos sigan siendo accesibles y que el sistema permanezca operativo.
- **Reducción de la latencia:** Un caché distribuido puede estar geográficamente más cerca de los usuarios, lo que reduce la latencia en el acceso a los datos. Por ejemplo, un usuario en Europa accediendo a datos que también están cachéados en un servidor europeo experimentará tiempos de respuesta más rápidos comparado con acceder a datos almacenados solo en servidores en EE. UU.
- **Consistencia de los datos:** Manejar la consistencia entre múltiples caches es uno de los desafíos en cachés distribuidos, especialmente en entornos donde los datos cambian frecuentemente. Se utilizan diferentes estrategias, como la coherencia eventual o la invalidación activa de caché, para asegurar que todos los nodos del caché tengan los datos más actualizados posible.

