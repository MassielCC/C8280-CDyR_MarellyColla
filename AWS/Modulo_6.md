# LAB 6: Asociar un volumen de EBS

## Tarea 1. Comenzar a crear la instancia y asignarle un nombre
- Sevicios > Informática > EC2 > Lanzar instancia

## Tarea 2. Imágenes de aplicación y SO
El tipo de imagen de máquina de Amazon (AMI) que selecciones determina el sistema operativo (SO) que se ejecutará en la instancia de EC2 que inicies. En este caso, has seleccionado Amazon Linux 2023 como SO invitado.

## Tarea 3. Elegir el tipo de instancia
El Tipo de instancia define los recursos de hardware asignados a la instancia. Este tipo de instancia tiene 1 unidad de procesamiento central virtual (CPU) y 1 GiB de memoria.

## Tarea 4. Seleccionar un par de claves
El par de claves vockey que has seleccionado te permitirá conectarte a esta instancia mediante SSH después de que se haya iniciado.

## Tarea 5. Configuración de red
![Configuración](image-28.png)
![Grupo de seguridad](image-29.png)

## Tarea 6. Configurar el almacenamiento
![Configurar almacenamiento](image-30.png)

## Tarea 7: Detalles avanzados
![Datos de usuario](image-31.png)

## Tarea 8: Revisar la instancia y lanzarla
![Detalles de instancia](image-32.png)

## Tarea 9. Acceder a la instancia de EC2
![Prueba 1](image-33.png)

## Tarea 10. Actualizar el grupo de seguridad
![Grupo de seguridad](image-34.png)

## Tarea 11: Crear una regla de entrada
![Reglas de entrada](image-36.png)

## Tarea 12. Probar la regla
![Prueba 2](image-35.png)

## Tarea 13: Adjuntar un volumen de EBS a la instancia de EC2
El volumen de EBS tiene que estar en la misma zona de disponibilidad que la instancia EC2

- Zona de disponibilidad :us-east-1c
![Zona y panel izquierdo](image-37.png)

![Crear volumen](image-38.png)

![Asociar instancia](image-39.png)

![Volumen asociado a instancia](image-40.png)