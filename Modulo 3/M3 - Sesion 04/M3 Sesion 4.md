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
