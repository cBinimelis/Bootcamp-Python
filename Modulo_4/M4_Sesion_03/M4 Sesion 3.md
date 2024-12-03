# Modulo IV - Sesión III

## Agenda

- ¿Qué es un diagrama de clases?
- ¿Para qué sirven los diagramas de clases?
- Notación de un diagrama de clases
- Tipos de relaciones entre clases
- Lectura y escritura de diagramas de clases

## ¿Qué es un diagrama de clases?

Es un tipo de diagrama que nos permite modelar de una manera estática las clases, sus atributos, métodos y las relaciones entre sí, para poder entender de una manera gráfica el funcionamiento de nuestro sistema.

## ¿Para qué sirven los diagramas de clases?

- Modelar
- Visión general
- Visión específica de los requerimientos
- Diagramar los elementos que interactúan

## Notación de un diagrama de clases

- Nombre de la clase
- Atributos
- Métodos
- Accessors
  - Publico: `+`
  - Privado `-`
  - Protegido `#`

## Tipos de relaciones entre clases

- Asociación
- Composición
- Agregación
- Dependencia
- Herencia

---

## Diagramas de clase

Un diagrama de clases en el Lenguaje Unificado de Modelado (UML) es un tipo de diagrama estático que describe la estructura de un sistema mostrando las clases, sus atributos, operaciones, y las relaciones entre los objetos.

### ¿Para qué se usan los diagramas UML?

Ilustrar modelos de datos para sistemas de información, y comprender mejor la visión general de los esquemas de una aplicación.

El diagrama de clases estándar está compuesto por tres partes:

- **Sección superior:** Contiene el nombre de la clase.
- **Sección central:** Contiene los atributos de la clase.
- **Sección inferior:** Incluye operaciones de clases (métodos).

### Niveles de acceso con sus símbolos correspondientes

- **Público (+):** Indica que el atributo será visible tanto dentro como fuera de la clase.
- **Privado (--):** Indica que el atributo sólo será accesible desde dentro de la clase.
- **Protegido (#):** Indica que el atributo no será accesible desde fuera de la clase.

### Tipos de Relación

Una relación identifica una dependencia. Esta dependencia puede ser entre dos o más clases

- **Multiplicidad** es el número de elementos de una clase que participan en una relación. Se puede indicar un número, un rango... Se utiliza n ó \* para identificar un número cualquiera.
  Por ejemplo:

  - 1..\*, que se lee de uno a muchos
  - 1..1, que se lee de 1 a 1
  - \*.. \*, que se lee de muchos a muchos

- **Asociación:** Este tipo de relación es el más común y se utiliza para representar dependencia semántica. Se representa con una simple línea continua que une las clases que están incluidas en la asociación.
- **Composición:** Hace referencia a una relación entre clases que indica pertenencia. Y uno es dependiente de la otra. Se representa con un rombo lleno en la clase cuya instancia contiene las instancias de la otra clase.
- **Agregación:** Es una representación jerárquica que indica a un objeto y las partes que componen ese objeto. Se representa con un rombo hueco en la clase cuya instancia es una agregación de las instancias de la otra.
- **Dependencia:** Una línea discontinua con una flecha apuntando a otra clase de dependencia.
- **Herencia:** Esta relación se representa como una línea continua con una flecha hueca en el extremo que apunta a la super clase.

### Guía para construir la Estructura de un Diagrama de Clases

- Identifica los nombres de las clase a partir de los objetos.
- Distinguir las relaciones entre clases
- Crea la estructura
- Identificar los atributos con su tipo de dato
- Identificar las operaciones

**Lectura de un Diagrama de Clases**

- Lectura de la estructura del objeto de la clase que está compuesto por tres partes
  - Sección superior Contiene el nombre
  - Sección central Contiene los atributos
  - Sección inferior Incluye operaciones
- Lectura de la multiplicidad de la clase
- Lectura de las relaciones que tengan estas clases
