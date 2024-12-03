# Módulo III - Sesión IV

## Agenda

- Conjuntos
- Estructuras Condicionales

## Conjuntos

Son estructuras similares a los conjuntos en matemáticas, albergando solamente datos únicos, los cuales no poseen un orden definido ni un formato indexado.

```python
#Declaracion informal
variable = {1, 5, 7, 9}
# Declaración formal
variable = set()
```

### Operadores

- .add()
- .remove
- Union `|`
- Interesccion `&`
- Diferencia `-`
- Diferencia Simétrica `^`
- `IN`

## Estructuras Condicionales

Las condiciones, como su nombre indica, se utilizan para distribuir las deciciónes en base a las condiciones presentadas en el código utilizando los respectivos operadores comparativos para definir si el resultado esperado es `True` o `False`

### Operadores

- `>`
- `<`
- `>=`
- `<=`
- `==`
- `!=`
- `in`

---

## Operadores lógicos

Los operadores lógicos se utilizan para tomar una decisión basada en múltiples condiciones. Los operadores lógicos utilizados en Python son and (y), or (o) y not (no).

El resultado de una operación lógica es true o false.

- True cuando la sentencia es verdadera y false cuando ésta es falsa.
- And devuelve true cuando ambos elementos son verdaderos, de lo contrario devuelve falso.
- Or devuelve true cuando alguno de los elementos es verdadero, de lo contrario devuelve falso
- Not devuelve true cuando la sentencia es falsa, o false cuando la sentencia es verdadera.

## Operadores de comparación

Los operadores de comparación se utilizan para comparar valores. Devuelve True o False según la condición.

- Operador mayor que ( `>` ), regresa true si el valor de la izquierda es mayor que el de la derecha.
- Operador menor que ( `<` ), regresa true si el valor de la izquierda es menor que el de la derecha.
- Operador igual que ( `==` ), regresa true si el valor de la izquierda es igual que el de la derecha.
- Operador no es igual que ( `!=` ), regresa true si el valor de la izquierda es diferente al de la derecha.
- Operador mayor o igual que ( `>=` ), regresa true si el valor de la izquierda es mayor o igual que el de la derecha.
- Operador menor o igual que ( `<=` ), regresa true si el valor de la izquierda es menor o igual que el de la derecha.

## Sentencias Básicas

- if (si condicional) Esta sentencia estudia si se cumple la condición que le sigue y devuelve true en caso de que se cumpla y false en caso contrario.
- else (en caso contrario) Esta sentencia siempre se usa para indicar que debe suceder en caso de que la sentencia if sea falsa, siempre y cuando no existan más condiciones posibles.
- elif (en caso contrario si) Esta sentencia se usa para indicar que hay que evaluar otra condición en caso de que el if tenga resultado falso. De esta manera podemos crear una cascada de expresiones a evaluar.
- El bucle for en Python se utiliza para iterar sobre una secuencia (lista, tupla, cadena) u otros objetos iterables. La iteración sobre una secuencia se denomina recorrido.
- El bucle while en Python se utiliza para iterar sobre un bloque de código mientras la expresión de prueba (condición) sea verdadera. Generalmente utilizamos este bucle cuando no sabemos de antemano el número de veces que hay que iterar.
- La sentencia break termina el bucle que la contiene.
- La sentencia continue se utiliza para saltar el resto del código dentro de un bucle sólo para la iteración actual.
