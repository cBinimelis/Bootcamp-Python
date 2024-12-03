# Módulo IV - Sesión I

## Agenda

- ¿Que es la orientación a objetos?
- Programación orientada a objetos
- Importancia de la orientación a objetos en la programación
- Diferencias con programación estructurada
- Orientación a objetos aplicada a la vida cotidiana
- ¿Qué es un objeto?
- ¿Qué es una clase?
- Diferencias entre clase, instancia y objeto
- Atributos de una clase
- Estado de un objeto
- Diferencia entre atributo y estado
- Métodos de una clase
- Comportamiento de un objeto
- Diferenca entre método y comportamiento
- Principios básicos
- Abstracción y encapsulamiento

### ¿Que es la orientación a objetos?

La orientacion a objetos es un paradigma de programacion que organiza el software como una coleccion de objetos, que son instancias de clases. En este paradigma, los objetos interactuan entre sí para resolver problemas y cada objeto puede representar cosas del mundo real o conceptos abstractos.

- **Objetos:** Son entidades que tienen atributos (características) y métodos (comportamientos).
- **Clases:** Son los planos o moldes a partir de los cuales se crean objetos.

**Ejemplo Cotidiano**
Pensemos en una "casa como un objeto. Las características de uma cas a(numero de habitaciones, color, tamaño) serían sus atributos, mientras que las acciones que puede realizar una casa (abrir puertas, encender luces, etc) serían sus métodos.

### Programación orientada a objetos

La POO s un estilo de programacion basado en el uso de obnjetos. En lugar de escribir funciones suletas, en la POO creamas clases que representan entidades, y los métodos y atributos de estas clases encapsulan datos y funcionalidades de manera lógica.

**Características clave de la POO**

- Modularidad: Los programas se dividen en módulos o clases.
- Reutilización: Una clase puede ser reutilizada en diferentes aprtes del programa o en otros programas.
- Mantenimiento: La POO facilita el mantenimiento de grandes proyectos de software, ya que permite cambiar o mejorar partes del codigo sin afectar otras.

### Importancia de la orientación a objetos en la programación

La POO es fundamental en la programación moderna porque:

- **Mejora la organización del código:** Al usar clases y onjetos, el código es más fácil de leer y mantener.
- **Facilita el trabajo en equipo:** Los proyectos se pueden dividir en múltiples clases o módulos, lo que permite a varios programadores trabajar de manera simultánea.
- **Promueve la reutilización:** Las clases y los objetos pueden ser utilizados en diferentes partes de un proyecto o incluso en otros proyectos.

**Ejemplo Cotidiano**
Imagina una empresa automotriz que fabrica autos. En lugar de construir cada auto desde cero, utilizan un plano (clase) para crear nuevos autos (objetos). Esto ahorra tiempo y asegura consistencia.

### Diferencias con programación estructurada

- **Programación estructurada:** Se basa en la ejecución secuencial de instrucciones con el uso de funciones y el control de flujo. Las funciones operan sobre datos globales, lo que puede complicar el mantenimiento.
- **POO:** Organiza el programa en torno a objetos, cada uno con sus propios datos (atributos) y comportamientos (métodos). Esto promueve el encapsulamiento y hace más claro el diseño del software.

**Ejemplo Cotidiano**
En un programa estructurado, podrías tener funciones como `abrir_puerta(casa)`. En un enfoque orientado a objetos, tendrías una clase `Casa` con el método `abrir_puerta()`, que automáticamente sabe cuál casa está afectando.

### Orientación a objetos aplicada a la vida cotidiana

La POO se inspira en cómo interactuamos con el mundo. Por Ejemplo:

- Un coche es un objeto con atributos (color, velocidad, combustible) y métodos (acelerar, frenar).
- Un teléfono es un objeto con atributos (marca, modelo) y métodos (llamar, enviar mensajes).

### ¿Qué es un objeto?

Un objeto es una instancia de una clase, una representación concreta ade algo que puede existir en el mundo real o en un contexto abstracto.

**Ejemplo**
En una aplicación de biblioteca, un "libro" sería un objeto que podría tener atributos como título, autor y número de páginas.

### ¿Qué es una clase?

Una clase es el molde o plano a partir del cual se crean los objetos. Define los atributos (datos) y métodos (funcionalidades) que tendrá cada objeto.
**Ejemplo**
Si piensas en una clase "Auto", puedes tener atributos como `marca`, `modelo` y `color`. Cada objeto creado a partir de esa clase sería un auto específico con esos atributos.

### Diferencias entre clase, instancia y objeto

- **Clase:** El plano o molde de algo (ej: "Auto").
- **Objeto:** Una representación concreta creada a partir de una clase (ej. un auto específico)
- Instancia: Es el término que se usa para referirse a un objeto creado a partir de una clase.

**Ejemplo Cotidiano**
Clase: "Gato" (define características generales de los gatos). Objeto: "Gato de Juan" (una instancia específica de la clase `Gato`)

### Atributos de una clase

Los atributos son las características o propiedades que definen un objeto. Se dividen en dos categorías:

- **Atributos de instancia:** Son atributos propios de cada objeto.
- **Atributos de clase:** Son compartidos por todas las instancias de una clase.

### Estado de un objeto

El estado de un objeto es el valor actual de sus atributos. El estado puede cambiar a lo largo de la vida del objeto.

**Ejemplo**
Un objeto "Auto" puede tener el estado `color: rojo`, `velocidad: 0 km/h`. Si el auto acelera, su estado cambia a `velocidad: 60 km/h`

### Diferencia entre atributo y estado

- Atributo: La propiedad o característica de un objeto.
- Estado: Los valores actuales de esos atributos en un momento determinado.

**Ejemplo**
Un libro puede tener el atributo "páginas". El estado de ese atributo en un momento puede ser "página 45"

### Métodos de una clase

Los métodos son las funciones o comportamientos que puede realizar un objeto. Definen qué puede hacer un objeto y cómo interactúa con otros objetos.

### Comportamiento de un objeto

El comportamiento de un objeto es el conjunto de acciones que puede realizar, determinadas por sus métodos.

**Ejemplo**
Un objeto "perro" puede tener el comportamiento de "ladrar" o "correr". Estos comportamientos son métodos dentro de la clase `Perro`.

### Diferenca entre método y comportamiento

El método en sí es un algoritmo asociado a un objeto (o una clase de objetos), cuya ejecución se desencadena tras la recepción de un "mensaje". Mientras que el comportamiento, es lo que el objeto puede hacer. Un método puede producir un cambio en las propiedades del objeto, o la generación de un "evento" con un nuevo mensaje para otro objeto del sistema.

### Principios básicos

- **Abstracción:** Permite representar objetos de manera simplificada, mostrando solo los detalles relevantes y ocultando lo innecesario.
- **Encapsulamiento:** Protege los datos internos de un objeto, restringiendo el acceso directo a ellos y permitiendo solo a través de los métodos.

---

## Paradigma de la orientación a Objetos

La programación orientada a objetos es un paradigma de programación, es decir, un modelo o un estilo de programación que nos da unas guías sobre cómo trabajar con él. Se basa en el concepto de clases y objetos. Este tipo de programación se utiliza para estructurar un programa de software en piezas simples y reutilizables de planos de código (clases) para crear instancias individuales de objetos.

- Permite que el código sea reutilizable, organizado y fácil de mantener.
- Evita duplicar el código y crea de esta manera programas más eficientes.
- Evita el acceso no deseado a los datos o la exposición de código propietario mediante la encapsulación y la abstracción.
- Ayuda en sistemas grandes estando orientada a pensar en las relaciones o interacciones de los diferentes componentes del sistema.
- Agiliza el desarrollo de software.

### Programación Estructurada

- Separa los datos de las funciones
- Pretende resolver un problema de principio a fin en una sola estructura de código.

### Programación Orientada a Objetos

- Define un conjunto de objetos donde se combinan de forma modular los datos con las funciones
- Declara como variables a los tipo de datos de los objetos del problema, y a su vez, existe la posibilidad de que cada objeto contenga a otro objeto o función anidada.
- Resuelve los problemas identificando a los actores que tienen participación en el mismo, e identificando también sus acciones.

### Objetos y métodos

Un objeto es una entidad que agrupa un estado y una funcionalidad relacionadas. El estado del objeto, se define a través de variables llamadas atributos, mientras que la funcionalidad se modela a través de funciones a las que se les conoce con el nombre de métodos del objeto.

### Estado de un objeto

El estado de un objeto abarca todas las propiedades del objeto, y los valores actuales de cada una de esas propiedades.

### Comportamiento de un objeto

El comportamiento es la manera en que una clase de objetos puede hacer cualquier cosa para sí o para otros objetos.

### Diferencias entre Atributos y Estados

- Los **atributos** son las propiedades o características del objeto.
- El **estado** de un objeto viene definido por los valores que toma en un instante determinado los atributos que define al objeto.

### Métodos en las clases

Son las funcionalidades asociadas a los objetos, que son implantadas o programadas dentro de las clases.

- **Encapsulación :** Es el proceso en el cual se comparten los elementos de una abstracción que constituyen su estructura y comportamiento.

  - Estándar
  - Abierto
  - Protegido
  - Semi cerrado
  - Cerrado

- **Abstracción :** Consiste en aislar un elemento de su contexto o del resto de los elementos que lo acompañan.
  **Los procesos, funciones y métodos, pueden ser abstraídos**.
- **Método :** Es lo que el objeto puede hacer. Un método puede producir un cambio en las propiedades del objeto.
- **Comportamiento :** El comportamiento permite que los objetos se comuniquen entre sí por medio de sus métodos
