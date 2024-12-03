# Modulo IV - Sesión VIII

## Agenda

- Manejando archivos con Python

## Manejando archivos con Python

### ¿Por qué necesitamos manejar archivos?

En general, dividimos los archivos en dos categorías cuando se trabaja con Python: texto y binarios. Mientras que los archivos de texto son texto simple, los archivos binarios contienen datos que solo pueden ser interpretados por un ordenador. Python ofrece formas simples de manipular ambos tipos de archivos.

### Apertura de archivos

Existen dos formas básicas de acceder a un archivo, una es utilizarlo como un archivo de texto, que procesaremos línea por línea; la otra es tratarlo como un archivo binario, que procesaremos byte por byte.

- En Python, para abrir un archivo usaremos la función open, que recibe el nombre del archivo a abrir.

Distintos modos de apertura

- **Modo sólo escritura posicionándose al final del archivo (a) :** En este caso no es posible realizar modificaciones sobre el archivo, solamente leer su contenido.
- **Modo de sólo escritura (w) :** En este caso el archivo es truncado (vaciado) si existe, y se lo crea si no existe.
- **Modo de sólo lectura (r) :** En este caso se crea el archivo, si no existe, pero en caso de que exista se posiciona al final, manteniendo el contenido original.
- **Modo r en la apertura de archivos Python :** El modo r se utiliza cuando queremos abrir el archivo para su lectura. El puntero de archivo en este modo se coloca en el punto de inicio del archivo. `f1 = open ('god.txt','r')`
- **Modo r+ en la apertura de archivos Python :**El modo r+ se puede utilizar en la función open() de la siguiente manera: `f1 = open ('god.txt','r+')`
- **Modo a en la apertura de archivos Python :** El modo a abre el archivo con el propósito de agregarlo. `f1 = open ('god.txt','a')`
- **Modo a+ en la apertura de archivos Python :** Modo a+ en la apertura de archivos Python. `f1 = open ('god.txt','a+')`
- **Modo w en la apertura de archivos Python :** Modo w en la apertura de archivos Python. `f1 = open ('god.txt','w')`
- **Modo w+ en la apertura de archivos Python :** El modo w+ abre el archivo para lectura y escritura.`f1 = open ('god.txt','w+')`
