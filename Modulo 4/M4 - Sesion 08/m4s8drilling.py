def crear_archivo():
    try:
        archivo = open("informacion.dat", "x")
        archivo.close()
    except FileExistsError:
        print("El archivo informacion.dat ya existe.")


def leer_archivo():
    try:
        archivo = open("informacion.dat", "r")
        lines = archivo.read()
        archivo.close()
        print(lines)
    except FileNotFoundError:
        print("No se ha encontrado el archivo deseado.")


crear_archivo()
leer_archivo()
