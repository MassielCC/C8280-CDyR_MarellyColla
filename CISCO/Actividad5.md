## Preguntas de Actividad 5

1. **¿Se utilizaron diferentes tipos de cables / medios para conectar dispositivos?**
   se utilizaron 2 tipos de cables: Cobre y serie DTE

 <p align="light"> 
  <img src="https://i.postimg.cc/Vvyfhdrz/actv5-1jpg.jpg)](https://postimg.cc/G8Qn83xf)" alt="FOTO ODS 7" width="600px" />
</p>
  
   
2. **¿Los cables cambiaron el manejo de la PDU de alguna manera?**
No, los cables en sí mismos no alteran el manejo de la PDU. La PDU se transmite a través de los cables según el protocolo de red utilizado, como Ethernet, y los cables simplemente facilitan la transmisión de datos sin modificar la PDU en sí misma.

3.	**¿El Hub perdió parte de la información que recibió?**
No, los hubs no pierden información de manera intencional. Sin embargo, debido a su naturaleza de difusión, todos los dispositivos conectados a un hub reciben todas las tramas de datos, lo que puede resultar en congestión y colisión de datos en la red, pero el hub no descarta intencionalmente ninguna información.

4.	**¿Qué hace el hub con las direcciones MAC y las direcciones IP?**
El hub no realiza ninguna acción específica con las direcciones MAC o IP. Simplemente retransmite los datos a todas las conexiones sin tener en cuenta las direcciones de destino. No realiza ningún análisis o filtrado basado en direcciones MAC o IP.

5.	**¿El punto de acceso inalámbrico hizo algo con la información que se le entregó?**
Sí, el punto de acceso inalámbrico (AP) empaqueta la información como marcos inalámbricos para su transmisión a través de la red inalámbrica. Esto implica encapsular los datos en un formato adecuado para la transmisión inalámbrica y realizar la gestión de la conexión con los dispositivos inalámbricos que se conectan a él.

6.	**¿Se perdió alguna dirección MAC o IP durante la transferencia inalámbrica?**
Sí se perdió la información un 25% en el envió a la laptop Porque el mensaje que se envía es a larga distancia, la información tendera a perderse en algún punto.

<p align="light">
  <img src="https://i.postimg.cc/qvX8nXcr/Imagen1.png)](https://postimg.cc/fVytQdgq)" alt="FOTO ODS 7" width="600px" />
</p>

7.	**¿Cuál fue la capa OSI más alta que utilizaron el hub y el punto de acceso?**
La capa más baja que utilizaron es la Capa 1, que corresponde a la Capa Física del modelo OSI.

8. **¿El hub o el punto de acceso reprodujeron en algún momento una PDU rechazada con una “X” de color rojo?**
Si, cuando se envía el mensaje pasa por el Hub y llega a 172.16.31.3

9. **Al examinar la ficha PDU Details (Detalles de PDU), ¿qué dirección MAC aparecía primero, la de origen o la de destino?**
Primero aparece la dirección MAC del destino

10. **¿Por qué las direcciones MAC aparecen en este orden?**
Si el destino aparece primero en la lista, un switch puede comenzar a reenviar una trama a una dirección MAC conocida más rápidamente

11. **¿Había un patrón para el direccionamiento MAC en la simulación?**
No
12. **¿Los switches reprodujeron en algún momento una PDU rechazada con una “X” de color rojo?**
No
13. **Cada vez que se enviaba la PDU entre las redes 10 y 172, había un punto donde las direcciones MAC cambiaban repentinamente. ¿Dónde ocurrió eso?**
Ocurrió en el router
14. **¿Qué dispositivo usa direcciones MAC que comienzan con 00D0: BA?**
El router
![Dirección MAC](img/imagen1.jpg)

15. **¿A qué dispositivos pertenecían las otras direcciones MAC?**
    
<p align="justify">
Las otras direcciones MAC pertenecían a dispositivos como: laptop-PT y  PC-PT.
 </p>
 
16. **¿Las direcciones IPv4 de envío y recepción cambiaron los campos en alguna de las PDU?**
    
<p align="justify">
En el caso de las direcciones IPv4, los campos de envío y recepción no cambian en ninguna de las PDU (Protocol Data Unit).
 </p>
 
17. **Cuando sigue la respuesta a un ping, a veces llamado pong, ¿ve el cambio de envío y recepción de direcciones IPv4?**
    
<p align="justify">
  
Sí, al seguir la respuesta a un ping, se puede observar el cambio de envío y recepción de direcciones IPv4.
 </p>
 
18. **¿Cuál es el patrón para el direccionamiento IPv4 utilizado en esta simulación?**
    
<p align="justify">
  El patrón para el direccionamiento IPv4 utilizado en esta simulación son: 10.10.10.2 / 24, 10.10.10.3 /24, 172.16.31.2 / 24, 172.16.31.3 / 24, 172.16.31.4 / 24, 172.16.31.5 / 24.
 </p>
 
19. **¿Por qué es necesario asignar diferentes redes IP a los diferentes puertos de un router?**
    
<p align="justify">
  Es necesario para segmentar el tráfico de red y mantener la seguridad al separar las comunicaciones de diferentes dispositivos o redes.
 </p>
 
20. **Si esta simulación se configura con IPv6 en lugar de IPv4, ¿cuál sería la diferencia?**

<p align="justify">
  Si se configura con IPv6 en lugar de IPv4, la diferencia principal sería el uso de direcciones IPv6, que son mucho más largas y permiten un número mucho mayor de direcciones únicas en comparación con IPv4. Además, IPv6 tiene características de seguridad y autoconfiguración mejoradas en comparación con IPv4.
 </p>

[VIDEO DE LA ACTIVIDAD](https://drive.google.com/file/d/1Tlcle0xfso9_v0IXUv7ozB1l3iiOEh-A/view?usp=sharing)

