def crear_archivo():
    try:
        archivo = open("informacion.dat", "x")
        archivo.close()
    except FileExistsError:
        print("El archivo informacion.dat ya existe.")


crear_archivo()
