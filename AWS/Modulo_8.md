# Modulo 8: Seguridad

**4 áreas de seguridad en informática en la nube**
- **Datos:** Protección de la información almacenada y procesada en la nube
- **Permisos:** Regulación de quién tiene acceso a los recursos y datos en la nube
- **Infraestructura:** Protección de las máquinas y el hardware que ejecutan, almacena y procesan datos en la nube
- **Evaluación:** inspección de la infraestructura, los permisos y los datos para asegurarnos de que están seguros.

**Denegación de servicio distribuido (DDoS)**
Intento malicioso de hacer que un sistema dirigido, como un sitio web o una aplicación no esté disponible para los usuarios finales. 

Utilizan varias técnicas para consumir recursos de red u otro tipo de forma que interrumpe el acceso de los usuarios finales legítimos. 

**AWS Shield --> ataques a infraestructura**
Servicio de protección contra DDoS administrado que protege las aplicaciones que se ejecutan en AWS. Trabaja en conjunto con Elastic Load Balancing, Amazon CloudFront y Amazon Route 53

- **AWS Shield Standard**
Disponible sin costo adicional. Protege a los usuraios de los ataques DDoS más comunes
    
- **AWS Shield Advanced**
Ataques volumétricos, detección inteligente de ataques y mitigación en las capas de la aplicación y la red.
    
**AWS WAF -->  ataques a infraestructura**
Servicio que el da control sobre qué tráfico permitir o bloquear en sus aplicaciones web mediante la definición de reglas de seguridad web personalizables.

**Amazon Inspector**
Un servicio de evaluación de seguridad automatizada. 
Monitorea los servicios y proporciona actualizaciones sobre cualquier vulnerabilidad.

Funciona ejecutando una evaluación en sus instancias EC2:
    1. Comprueba varias prácticas recomendadas predeterminadas. 
    2. Elabora una lista detallada de los resultados de seguridad priorizados por nivel de severidad. 
    3. Los resultados se pueden revisar directamente o como parte de informes de evaluación 
    
Ayuda a verificar si hay accesibilidad a la red NO DESEADA de sus instancias EC2 y el estado de seguridad de las aplicaciones que se ejecutan en las instancias.

**AWS Artifact**
Recurso centralizado para la información relacionada con la conformidad. Proporciona acceso a los informes de seguridad y  de los estándares de conformidad que cumplen.

---
**Elastic Load Balancing - ELB**
Es un servicio de Amazon que distribuye automáticamente el tráfico entrante de forma eficiente entre un grupo de servidores backend de manera que se incrementa la velocidad y el rendimiento. Ayuda a mejorar la escalabilidad de una aplicación.

Tipos:
- Balanceador de carga de aplicaciones
- Balanceador de carga de Gateway
- Balanceador de carga de red