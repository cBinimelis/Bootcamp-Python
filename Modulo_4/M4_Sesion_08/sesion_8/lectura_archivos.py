def leer_archivo():
    try:
        archivo = open("datos.csv", "r")
        contenido = archivo.read()
        archivo.close()
        print(contenido)
    except FileNotFoundError:
        print("No se encuentra el archivo datos.cvs")
    except Exception as error:
        print("Se hya generado un error no previsto: ", error)


leer_archivo()
