def reemplazar_datos(dato_antiguo, dato_nuevo):
    conteo = 0
    try:
        archivo = open("informacion.dat", "r")
        reemplazo = ""
        for linea in archivo:
            cambios = linea.replace(dato_antiguo, dato_nuevo)
            reemplazo = reemplazo + cambios + "\n"
            conteo += 1
        archivo.close()

        archivo_reemplazo = open("informacion.dat", "w")
        archivo_reemplazo.write(reemplazo)
        archivo_reemplazo.close()
    except FileNotFoundError:
        print("No se ha encontrado el archivo informacion.dat")
    except Exception as e:
        print("ha ocurrido un error inesperado", e)
    finally:
        print(f"Se ha remplazado satisfactoriamente {conteo} reemplazos")


print("Hola Mundo")
reemplazar_datos("Información", "Procesamiento")
