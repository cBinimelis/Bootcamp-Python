# Modulo VI - Sesión II

## Agenda

- Entorno virtual

## Entorno virtual

Con el fin de facilitar el despliegue, se crea un entorno aislado para realizar pruebas. Lo ideal sería disponer de un entorno local lo más parecido posible al entorno remoto.

### MVC en Django para aplicaciones monolíticas

Una aplicación monolítica es un sistema de aplicaciones en el que todos los módulos relevantes se empaquetan como una única unidad de ejecución que se puede implementar.

- Modelos (Datos y Lógica): Representa y mantiene los datos de la aplicación en la base de datos. Cómo se almacena la información y cómo se puede recuperar.
- Vistas (interfaz de usuario): muestra los datos que utilizan el modelo al usuario, como una salida o una GUI.
- Controlador (administrador de requests): maneja la solicitud del usuario y actúa como una interfaz entre modelos y vistas.

### Herencia de componentes en el modelo Mvc

La herencia facilita la creación de objetos a partir de otros ya existentes, obteniendo características (métodos y atributos) similares a los ya existentes.

### El principio dry y su aplicación en el entorno

El principio No te repitas (en inglés Don't Repeat Yourself o DRY, también conocido como Una vez y sólo una) Según este principio toda pieza de información nunca debería ser duplicada debido a que la duplicación incrementa la dificultad en los cambios y evolución.

### ¿Qué son los templates de django?

Las template tags de Django nos permiten comunicar elementos de Python a HTML, para que puedas construir sitios web dinámicos más rápido y fácil.

### Renderización en django

La renderización en Django se utiliza en las capas de plantillas, enviando la capa de datos a la capa de plantilla, luego renderizando la plantilla y finalmente devolviendo la solicitud de respuesta a través de la función HttpResponse.
