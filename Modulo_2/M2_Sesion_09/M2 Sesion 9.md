# Módulo II - Sesión IX

## Agenda

### Sincrónica

- Funciones
- Arreglos
- Bucles

### Asincrónica

- ¿Qué es el DOM?
- Cambio de ejecución
- ¿Qué es un evento?
- Tipos de evento

## Funciones

Las funciones son fragmentos de código que se repetirá varias veces dentro de la ejecución del codigo. La principal tarea de una funcion, es la de ahorrar el trabajo de tener que repetir dicho código cada vez quye se requiera utilizarlo.
La estructura básica de una función es la siguiente:

```javascript
function nombreFuncion(variable) {
  // Codigo a ejecutar
}
```

## Arreglos

Son la estructura de datos más básica que existe en JavaScript. Admiten datos de cualquier tipo, pudiendo almacenar la información en distintas dimensiones

## Bucles

Son bloques de codigos que se ejecutarán repetidamente de manera automática siempre y cuando se haya cumplido con la condición necesaria para su ejecución

La estructura básica de un bucle `for` es la siguiente:

```javascript
for (let i = 0; i < 10; i++) {
  console.log(i);
}
```

---

## Manipulación del DOM con JavaScript

### ¿Qué es el DOM?

El modelo DOM (Modelo de Objetos de Dominio o Document Object Model) es una API para HTML y XML, la cual entrega una representación estructural de los documentos en forma de árbol de nodos. Cada elemento corresponde a un nodo y cada texto en un nodo de texto.

A través del DOM y JavaScript se puede acceder a cualquiera de los elementos del árbol de nodos, alterar sus propiedades e invocar sus métodos. Así, es posible acceder a cualquier elemento de una página web, modificarlos, eliminarlos, añadir nuevos elementos, etc.

### Cambio de ejecución

Comúnmente, las aplicaciones se ejecutan de manera lineal, esto quiere decir que siempre se ejecutan desde arriba hacia abajo, sin embargo, actualmente predomina el modelo de programación basada en eventos, en el cual los programas no realizan ninguna acción hasta que se produzca un evento y recién ahí ejecutan alguna tarea que se desencadena con aquel evento. Una vez terminado el evento siguen en espera a la ocurrencia de algún nuevo evento.

### ¿Qué es un evento?

Un evento es alguna acción que realice el usuario que gatille algún proceso, por ejemplo, apretar un botón que muestre un texto antes oculto. Este se mantendrá oculto hasta que el usuario accione la visualización a través de un evento especifico, por ejemplo, haciendo clic sobre el botón y no antes.

### Tipos de evento

El nombre de los eventos se construye mediante el prefijo on, seguido del nombre en inglés de la acción que se realizará, por ejemplo, al hacer clic con el ratón, el evento se denomina onclick().

Para que un evento realmente sea útil, debe ser asociado a una función o código JavaScript. De esta forma, cuando se produce un evento se ejecuta el bloque de instrucciones que hemos indicado, activando aquellos mensajes, cambios de estilos, envíos de formularios, entre otras acciones que se pueden gatillar.
