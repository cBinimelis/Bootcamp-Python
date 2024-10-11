def escribir_archivo():
    try:
        archivo = open("informacion.dat", "w")
        archivo.write("Este en una nueva línea en el archivo")
        archivo.write("agregando la segunda línea del archivo")
        archivo.write("finalizando la línea agregada")
        archivo.close()
    except FileNotFoundError:
        print("No se ha encontrado el archivo informacion.dat")
    except Exception as e:
        print("ha ocurrido un error inesperado", e)


print("Hola Mundo")
escribir_archivo()
