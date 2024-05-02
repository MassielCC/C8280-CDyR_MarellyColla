# **Actividad 2**
## 1. Configuración básica en el S1 
![Configuración de S1](img/Act2-S1config.png)

Verificar la configuración de contraseñas para el S1
![Ver configuración de S1](img/Act2-S1config-Verificar.png)

**¿ Cómo puedes verificar que ambas contraseñas se hayan configurado correctamente?**
Con el comando "show running-config | include password" podemos confirmar que tanto la contraseña de consola como la de modo privilegiado sí están bien configuradas. 

**Aviso MOTD**
![Aviso MOTD](img/Act2-S1-MOTD.png)

**Configuración en la NVRAM**
![Configuración en la NVRAM](img/Act2-S1-NVRAM.png)

## 2. Configuración básica en el S2
![Configuración de S2](img/Act2-S2-config.png)

## 3. Configuración de la PC1 y PC2
### Para PC1
![Configuración de PC1](img/Act2-PC1-config.png)

### Para PC2
![Configuración de PC2](img/Act2-PC2-config.png)

### Probar conectividad a los switches
![Conectividad](img/Act2-PC1-conectividad.png)

**¿Tuviste éxito? Explica.**
No se tuvo éxito porque aún no hemos configurado las direcciones IP de los switches.

## 4. Configuración de la interfaz de administración  de switches

### Para S2
![IP de S2](img/Act2-S2-configIP.png)

**¿Por qué debe introducir el comando no shutdown?**
Para activar la interfaz vlan 1
![Verificar IP](img/Act2-S2-configIP-verificar.png)

## Verificar la conectividad de la red
### PC1 con PC2
![Conectividad con PC2](img/Act2-Conectividad-PC1-PC2.png)

### PC1 con S1
![Conectividad con S1](img/Act2-Conectividad-PC1-S1.png)

### PC1 con S2
![Conectividad con S2](img/Act2-Conectividad-PC1-S2.png)

### S1 con PC1, PC2 y S2
![Conectividad con S2](img/Act2-Conectividad-S1-Todos.png)