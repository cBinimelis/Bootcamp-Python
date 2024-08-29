# Módulo III - Sesión IV

## Agenda

- Paquetes
- Listas
- Diccionarios
- Tuplas
- Conjuntos

## Paquetes

Los paquetes sonmódulos que pueden ser creados para evitar repetir codigo que se utilizará frecuentemente

## Estructuras de datos

### Listas

Las listas son similares a los arreglos en otros lenguajes, cumpliendo la misma funcionalidad.

```python
# Informal
variable = ["elemento1", "elemento2", "elemento3"...]

# Formal
variable = list()
```

Las listas tienen métodos para modificar su funcionalidad y/o los elementos de la misma

- **.append(valor) :** Agrega un nuevo elemento a la lista.
- **.insert(i, valor) :** Recibe un índice y un valor, para poder inyectar el valor en el índice especificado, el valor previo se mueve al siguiente índice superior, así como todos los siguientes elementos.
- **.extend(lista) :** Agrega una lista de elementos a la lista desde la que se llama al método.
- **.remove(valor) :** Elimina el primer elemento en el cual se encuentre el valor recibido.
- **.pop() :** Elimina el último elemento
- **.pop(i) :** Elimina el elemento en el índice recibido
- **.clear() :** Elimina todos los elementos de la lista

Las listas tienen la característica de aceptar distintos tipos de datos dentro del mismo conjunto.

```python
listaQuimera = ["elemento1", 1, True, 17.0]
```

### Tuplas

Las tuplas son colecciones que almacenan pares valóricos.

```python
# Tuplas
variable = (valor1, valor2, valor3)
```

Se pueden imprimir de distintas maneras según lo que se requiera

```python
# Tupla completa
print(variable)
# (valor1, valor2, valor3)

# Elemento individual
print(variable[2])
# valor3

# Seleccion de elementos (se excluye el valor de cierre)
print(variable[1:4])
# (valor2, valor3, valor4)
```

### Diccionarios

Los diccionarios funcionan en relacion a una clave y un valor

```python
# Diccionarios
# Declaracion Informal
variable = {
    "key1": valor1,
    "key2": valor2,
    }

# Declaración Formal
variable = dict()
```

---

## Tipos de datos y secuencias básicas

### Variables

Para crear una variable, sólo tienes que asignarle un valor y luego empezar a utilizarla. La asignación se hace con un signo de igualdad (`=`)

`n = 100` Esto se lee o interpreta como "asigna a n el valor 100".

### Scope de variables

El lugar donde podemos encontrar una variable y también acceder a ella si es necesario se llama el scope de una variable. De esta manera hay variables locales y globales.

```python
# Variable global
s = "esta es una variable global"

def f():
    # Variable local
    S = "esta es una variable local"
```

### Tipos de datos

Entre los números tenemos los numeros enteros, estos son números tanto positivos como positivos. También contamos con los datos de punto flotante, estos son numeros tanto positivos como negativos, pero que incluyen valores decimales.

- **Cadena de Caracteres :** En Python cualquier cosa puede ser definido como una cadena si al declarar la variable encerramos el texto que deseamos entre comillas, bien sea dobles o simples. La cadena puede estar vacía siempre y cuando se abran y cierren las comillas.

  ```python
  print("soy una cadena")
  ```

- **Listas :** Una lista se crea colocando elementos dentro de corchetes y separados por comas. `[,]`
  ```python
  # Una lista de enteros
  mi_lista[1, 2, 3]
  ```
- **Diccionarios :** Crear un diccionario es tan sencillo como colocar los elementos dentro de llaves separadas por comas `{,}`. Un elemento tiene una clave y un valor correspondiente que se expresa como un par (clave: valor).

  ```python
  # Diccionario con claves tipo entero
  mi_diccionario = {1:'Manzana','pelota'}

  # Diccionario con claves mixtas
  mi_diccionario2 = {'nombre':'Juan', 1: [2, 4, 3]}
  ```

- **Tuplas :** Una tupla se crea colocando todos los elementos dentro de paréntesis separados por comas `(,)`. Puede tener cualquier número de elementos y éstos pueden ser de diferentes tipos (entero, flotante, lista, cadena, etc.).

  ```python
  # Tupla de numeros enteros
  mi_tupla = (1, 2, 3)
  print(mi_tupla)

  Resultado:
  (1, 2, 3)
  # tupla con tipos de datos mixtos
  mi_tupla = (1, “Hola”, 3.4)
  print(mi_tupla)
  Resultado:
  (1, ˈHolaˈ, 3.4)
  ```

- **Tuplas :** Un conjunto se crea colocando todos los elementos dentro de llaves, separados por comas `{,}`, o utilizando la función incorporada `set()`.
  Puede tener cualquier número de elementos y éstos pueden ser de diferentes tipos (entero, flotante, tupla, cadena, etc.). Pero un conjunto no puede tener elementos mutables como listas, conjuntos o diccionarios.

  ```python
  # conjunto de enteros
  mi_conjunto = {1, 2, 3}
  print(mi_conjunto)

  Resultado:
  {1, 2, 3}
  # conjunto de tipos de datos mixtos
  mi_conjunto = {1.0, “Hola”, (1, 2, 3)}
  print(mi_conjunto)
  Resultado:
  {1.0, “Hola”, (1, 2, 3)}
  ```
