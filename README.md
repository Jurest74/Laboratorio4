# Laboratorio4
Para la ejecución del código presentado a continuación deberá contar con la instalación de python en su computador, si no lo tiene descarguelo en el siguiente enlace
antes de continuar: https://www.python.org/downloads/

En el directorio raiz de este repositorio encuentra dos proyectos, clients y subscribers. A continuación se explica el objetivo de cada uno, su función y la manera de ejecutarlo.

Simulación de un gestor de tareas para procesamiento distribuido: Tenemos
un conjunto de clientes que tienen cada uno tareas para procesar (task_i) y tenemos un
conjunto de servidores que ejecutan esas tareas (task_i). Los clientes (publishers) envían a
una cola las tareas específicas a procesar, estas tareas son almacenadas en una cola del
MOM. Los servidores (subscribers) van tarea por tarea a la cola a retirar una task_i
específica y ejecutarla. Una vez un servidor termina una tarea específica notificará por otro
medio al cliente específico. En síntesis:
1. Cola: Almacenamiento en el MOM donde se depositan las tareas.
2. Mensaje: Identificador de la tarea, el username y el email para notificación
3. Cliente: Publisher que envía tareas a la cola.
4. Server: Subscribe quien extrae uno a uno tareas de la cola.

<h3><Ejecución</h3>
  
  
