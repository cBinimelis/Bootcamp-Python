# Módulo IV - Sesión II

## Agenda

- Creación de una Clase en Python
- Definición de Atributos
- Definición de Métodos
- Método Constructor
- Métodos Accesadores y Mutadores
- Colaboración y Composición

## Creación de una Clase en Python

La sintaxis para crear clases en python se inicia con la palabra reservada `class`, seguido del nombre de la clases en UpperCamelCase y el símbolo de dos puntos, esto quedaría de la siguiente manera;

```python
class NombreClase:
    pass
```

Una buena práctica es mantener cada clase en su archivo independiente, esto facilita su organización y claridad dentro del código.

## Método constructor

Es un método que instancia al objeto que se produce por medio de la clase, la sintaxis de los constructores es de la siguiente manera;

```python
class Animal:

    def __init__(self):
        pass
```

---

## Programación orientada a objetos

### La Clase

Una clase es un conjunto esencial de elementos que contienen un estado. Tanto propiedades, como atributos, comportamientos y métodos son lo que llamaremos clase.

Para construir una clase en Python se representa de una manera muy sencilla, comenzamos con la palabra reservada “CLASS”.

Seguidamente vamos a emplear el nombre de la clase por defecto, para ello deberemos de utilizar letras mayúsculas.

Partiendo de la definición de una clase, vamos a emprender la escritura de cada uno de los atributos, debemos dejar la sangría correspondiente de 4 ítems o la identación correspondiente a Python.

- **Crear un comportamiento:** Para crear el comportamiento de una clase en Python también conocidos como métodos, se definen con una función en Python con la palabra reservada "DEF". Para definir un comportamiento escribiremos "SELF"
- **El parámetro "PASS":** Cuando empleamos este parámetro significa que estamos creando el método. Para instanciar el "método constructor init", vamos a definir "DEF" y seguidamente la palabra "INIT".
- **Instanciar una Clase:** Para instanciar una clase, debemos crear un objeto. Al hacerlo, debemos emplear el simbolo es igual, para especificar que el enlace pertenece al objeto que acabamos de crear.
- **Imprimir:** Para imprimir por pantalla simplemente utilizamos el método "PRINT"

## Los Métodos

Los métodos que acceden a los datos de los objetos son, los métodos accedores y mutadores.
Los accedores se utilizan para acceder a los datos ocultos del objeto de este método, no cambia los datos o estado del objeto, por defecto son el “GET” (dame).
Los mutadores , son los métodos que pueden modificar o mutar el estado de un objeto, se definen con la palabra “SET”.
