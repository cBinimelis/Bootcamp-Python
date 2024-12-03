# Módulo III - Sesión VII

## Agenda

- Control de Flujo

## Control de flujo en Python

### Apertura modo lectura

Los ciclos son un elemento de programación que repite una porción de código un número determinado de veces hasta completar el proceso deseado.

**Creando un ciclo _while_**
Recordemos la sintaxis de la sentencia for

```python
for elem in secuencia:
    instrucciones del bucle
```

**Instrucción _for_**
Recordemos la sintaxis de la sentencia while

```python
while expresion_de_prueba:
    Cuerpo del while
```

### Evaluando condiciones en flujos

- Las condiciones se van evaluando en el orden en que aparecen escritas, de esta manera, si la primera condicion es falsa, se considera que toda la expresión es falsa y el ciclo se detiene, en caso de ser verdadera se evalúa la proxima condicion tomando en cuenta el operador logico (and, or y not).
- Si la segúnda condicion es falsa tomando en cuenta el operador logico entre ellas se considera que toda la expresión es falsa y se detiene el ciclo, en caso de ser verdadera se evalúa la proxima condicion tomando en cuenta el operador logico.
- Así sucesivamente, hasta llegar a la última condición y en caso de que esta sea verdadera se ejecuta el cuerpo del ciclo.

### Ciclos infinitos

Un ciclo infinito en python es un bucle condicional continuo y repetitivo que se ejecuta hasta que un factor externo interfiere en el flujo de ejecución, como una memoria insuficiente de la CPU, un código/funcion fallido que detuvo la ejecución, o una nueva funcion en los otros sistemas heredados que necesita la ejecucion del codigo.

### Utilizando ciclos anidados

Si un ciclo existe dentro del cuerpo de otro ciclo, se denomina _ciclo anidado._ La sintáxis básica de un ciclo anidado en Python es:

```python
#Bucle exterior
for variable in secuencia_uno:
    #Bucle interior
    for variable_interna in secuencia_dos:
        <cuerpo de codigo>
```

La sintaxis para anidar un bucle while es:

```python
while expresion_externa:
    #Opcional
    <cuerpo de codigo>
    #Bucle interior
    while expresion_interna
        <cuerpo de codigo>
```

### Combinación de ciclos con instrucciones if/else

Dentro de un ciclo **for** y/o **while**, se pueden utilizar sentencias if, elif y else. Cada ciclo puede tener una serie de acciones condicionales que pueden ser determinadas con las sentencias if.

### Utilizando las sentencias break y continue

Una sentencia break puede colocarse dentro de un bucle anidado. Si una sentencia break aparece en un bucle anidado, sólo el ciclo interior dejará de ejecutarse. Puedes usar una sentencia continue en Python para saltarte parte de un ciclo cuando se cumple una condición. Entonces, el resto del ciclo continuará ejecutándose. Las sentencias continue se utilizan dentro de los ciclos, normalmente después de una sentencia if.
