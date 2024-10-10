from io import open


def crear_archivo():
    try:
        archivo = open("datos.csv", "x")
        archivo.close()
    except FileExistsError:
        print("Archivo ya existe")
    except Exception as error:
        print("Se ha generado un error no previsto: ", error)


crear_archivo()
