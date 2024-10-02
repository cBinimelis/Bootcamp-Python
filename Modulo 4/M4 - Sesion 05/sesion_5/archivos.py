base_datos = open("datos.txt", "r")

# print(f"Nombre: {base_datos.name}")
# print(f"Modo: {base_datos.mode}")
# print(f"Status: {base_datos.closed}")
# contenido = base_datos.read()
# print(contenido)
# base_datos.close()
# print(f"Status: {base_datos.closed}")


for linea in base_datos:
    columnas = linea.split(",")
    print(columnas)

archivo = open("nuevo_archivo.txt")
