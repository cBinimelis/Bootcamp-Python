- Verificar si tenemos instalados los siguientes paquetes:
  | Instrucción | Comando |
  | ------------ | ----------- |
  | Python 3 | `python -V` |
  | pip | `pip -V` |
  | mkvirtualenv | `pip list` |

| Instrucción                                        | Comando                              |
| -------------------------------------------------- | ------------------------------------ |
| Crear un entorno virtual llamado: proyecto_django. | `py -m venv proyecto_django`         |
| Activar el entorno                                 | `.\proyecto_django\Scripts\activate` |
| Mostrar los paquetes instalados el entorno virtual | `pip list`                           |
| Instalar Django en el entorno virtual creado       | `pip install Django`                 |
| Verificar qué versión de Django se instaló.        | `pip list`                           |
| Mostrar cuál es el comando de ayuda de PIP.        | `pip -h`                             |
