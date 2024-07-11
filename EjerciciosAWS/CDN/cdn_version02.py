# IMPLEMENTAMOS LA CONEXIÓN DE LOS ARCHIVOS HTML CON EL CACHÉ

import time
import os
import webbrowser

class CDN:
    def __init__(self, max_cache_size, cache_expiration):
        self.cache = {}  # Diccionario para almacenar el contenido en caché
        self.max_cache_size = max_cache_size  # Tamaño máximo de la caché
        self.cache_expiration = cache_expiration  # Tiempo de expiración de la caché

    def read_and_open_html(self, filename):
        folder = os.getcwd()  # Obtiene el directorio actual de trabajo
        ruta= folder + "/folder/"
        full_path = os.path.join(ruta, filename)  # Construye la ruta completa del archivo
        print(full_path)
        if os.path.exists(full_path):  # Verifica si el archivo existe
            webbrowser.open('file://' + os.path.realpath(full_path))  # Abre el archivo HTML en el navegador
        else:
            print(f"File {filename} does not exist.")

    def get_content(self, url):
        if url in self.cache:  # Verifica si la url está en la caché
            content, timestamp = self.cache[url] # Obtiene el contenido y el timestamp de la url
            if time.time() - timestamp < self.cache_expiration: # Verifica si el contenido en la caché ha expirado
                print("Content served from cache")
                return content  # Devuelve el contenido de la caché si no ha expirado
            else:
                print("Cache expired, fetching new content")
                self.cache.pop(url)  # Elimina el contenido expirado de la caché
        self.read_and_open_html(url)        
        content = self.fetch_from_origin(url)  # Obtiene el contenido del servidor de origen

        self.add_to_cache(url, content)  # Añade el contenido a la caché
        return content

    def fetch_from_origin(self, url):
        print("Fetching content from origin server...")
        time.sleep(2)  # Simula el tiempo de respuesta del servidor de origen
        return f"Content of {url}"  # Devuelve el contenido simulado del servidor de origen
 
    def add_to_cache(self, url, content):
        if len(self.cache) >= self.max_cache_size:
            self.evict_cache()  # Evicta la entrada más antigua si la caché está llena
        self.cache[url] = (content, time.time())  # Añade el contenido a la caché con el timestamp actual
    
    def evict_cache(self):
        # Evict the oldest cache entry
        oldest_url = min(self.cache, key=lambda k: self.cache[k][1])
        print(f"Evicting cache for {oldest_url}")
        self.cache.pop(oldest_url)  # Elimina la entrada más antigua de la caché
    
    def __str__(self):
        return str(self.cache)  # Devuelve una representación en cadena de la caché

# Simulación de la CDN
def main():
    cdn = CDN(max_cache_size=3, cache_expiration=20)  # Crea una instancia de la clase CDN con tamaño máximo de caché y expiración
    while True:
        command = input("Enter command (get, exit): ")
        if command == 'get':
            url = input("Enter URL to fetch: ")
            content = cdn.get_content(url)  # Obtiene el contenido de la URL solicitada
            print(content)
            print(cdn)
        elif command == 'exit':
            print(cdn)
            break  # Sale del bucle si el comando es 'exit'
        else:
            print("Invalid command")  # Informa si el comando es inválido
    

if __name__ == "__main__":
    main()  # Ejecuta la función main si el script se ejecuta directamente
