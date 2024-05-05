# Actividad 6: Crear una red con un switch y un router - Modo Físico
## 1 . Configura la topología de red
![Topología de Red](img/Act6-Parte1.png)

## 2. Configurar los dispositivos y verificar la conectividad

### Asignar direcciones IP estáticas a las PC
![PC-A Configuración](img/Act6-Parte2.png)

**¿Por qué los pings no fueron correctos?**
Porque aún no se han configurado ni el router ni el switch, y es a través de estos que se podrían comunicar la PC-A y la PC-B

### Configurar el router
![Router config1](img/Act6-Router1.png)

* Configura y activa las dos interfaces en el router.

![Config interfaces](img/Act6-Router2.png)

* Habilitar el enrutamiento IPv6, guardar configuración y configurar el reloj del router

![Configuración](img/Act6-Router3.png)

### Configurar el switch
![Configuración](img/Act6-Switch.png)

### Verificar la conectividad

* De PC-A ping a PC-B
![Conectividad-PC](img/Act6-ConectividadAB.png)

* De S1 a PC-B
![Conectividad-S1-PCB](img/Act6-ConectividadS1-B.png)

## 3. Muestra la información del dispositivo
### Muestra la tabla de routing en el router.
![Tabla de enrutamiento](img/Act6-Tabla_enrutamiento.png)

**¿Qué código se utiliza en la tabla de enrutamiento para indicar una red conectada directamente?**
Se usa la letra C

**¿Cuántas entradas de ruta están codificadas con un código C en la tabla de enrutamiento?**
Hay 2: 192.168.0.0 y 192.168.1.0

**¿Qué tipos de interfaces están asociadas a las rutas con código C?**
Están conectadas las interfaces GigabitEthernet0/0/0 y GigabitEthernet0/0/1

**Rutas IPv6**
![Rutas IPv6](img/Act6-RutasIPv6.png)

### Muestra la información de la interfaz en el R1.
* a) show interface g0/0/1
![Interface g0/0/1](img/Act6-Interface001.png)

**¿Cuál es el estado operativo de la interfaz G0/0/1?**
La interfaz está activa, el protocolo de línea también está activo

**¿Cuál es la dirección de control de acceso a los medios (MAC) de la interfaz G0/0/1?**
Es 0060.4731.8102

**¿Cómo se muestra la dirección de Internet en este comando?**
Se muestra como 192.168.1.1/24 (dirección IPv4)

* b) show ipv6 interface interface 
![Interface g0/0/1 ipv6](img/Act6-Interface001-ipv6.png)

### Muestra una lista de resumen de las interfaces del router y del switch
* a) Comando show ip interface brief en R1
![R1-show-interface](img/Act6-R1-showInterface.png)

* b) Comando show ipv6 interface brief en R1 
![R1-show-interface-ipv6](img/Act6-R1-showInterface-IPv6.png)

* c)  Comando show ip interface brief en S1.
![S1-show-interface](img/Act6-S1-showInterface.png)

## Preguntas
**1. Si la interfaz G0/0/1 se mostrará administratively down, ¿qué comando de configuración de interfaz usaría para activar la interfaz?**
Usaría el comando ``no shutdown``

**2. ¿Qué ocurriría si hubiera configurado incorrectamente la interfaz G0/0/1 en el router con una dirección IP 192.168.1.2?**
No se podría enviar información a través del router