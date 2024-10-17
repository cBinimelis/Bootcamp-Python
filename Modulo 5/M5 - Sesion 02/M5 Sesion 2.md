# Modulo V - Sesión II

## Agenda

- Modelo Entidad - Relación
- Diseño conceptual del modelo entidad - relación

## Modelo Entidad - Relación

### Modelo Relacional

En este modelo todos los datos son almacenados en relaciones, y como cada relación es un conjunto de datos, el orden en el que estos se almacenen no tiene relevancia.

### Modelo Entidad Relación (ER)

Cuando se obtiene un modelo normalizado esto quiere decir que desde el punto de vista de la teoría se cuenta con un modelo optimizado en la redundancia de los datos e integridad.

El Modelo de Datos ER está basado en una percepción del mundo real que consta de entidades y relaciones. Las relaciones conforman tipos de dependencias entre las entidades.

En la práctica hay veces en que se debe desnormalizar el modelo para darle solución a la velocidad de respuesta a determinadas consultas, mantener datos de forma histórica o impedir que se modifiquen transacciones realizadas de forma indirecta.

### Formas normales

Proceso que consiste en designar y aplicar una serie de reglas a las relaciones obtenidas tras el paso del modelo entidad-relación al modelo relacional. Con objeto de minimizar la redundancia de datos, facilitando su gestión posterior.

- **Primera Forma Normal:** Una tabla está en primera forma normal si:
  - Sus atributos contienen valores atómicos (esto quiere decir que tienen que ser indivisibles)
- **Segunda Forma Normal:** Una tabla está en segunda forma normal si:
  - Está en primera forma normal.
  - Todos los atributos que no son clave primaria tienen dependencia funcional completa con respecto a todas las claves existentes en el esquema. Para recuperar un atributo no clave, se necesita acceder por la clave completa, no por una subclave.
- **Tercera Forma Normal:** Una tabla está en tercera forma normal si:
  - Está en segunda forma normal.
  - Todos los atributos que no son clave primaria no dependen transitivamente de esta
