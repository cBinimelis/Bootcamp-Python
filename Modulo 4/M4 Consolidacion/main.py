from vehiculos import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta
import csv

print("##### BIENVENIDO AL SISTEMA DE CONTROL DE VEHÍCULOS #####")
print("")


def parte_1():
    print("##---PARTE 1---##")

    print("Ingreso e impresión de instancias: \n")
    automoviles = []
    cantidad = int(input("¿Cuántos vehículos desea ingresar?: "))
    for i in range(cantidad):
        print(f"Datos del vehículo {i+1}: ")
        marca_n = input("Inserte la marca del automóvil: ")
        modelo_n = input("Inserte el modelo: ")
        nro_ruedas_n = int(input("Inserte el número de ruedas "))
        velocidad_n = int(input("Inserte la velocidad en km/h: "))
        cilindrada_n = int(input("Inserte el cilindraje en cc: "))

        automoviles.append(
            Automovil(marca_n, modelo_n, nro_ruedas_n, velocidad_n, cilindrada_n)
        )

    count = 1
    print("Imprimiendo por pantalla los Vehículos: \n")
    for auto in automoviles:
        print(f"Datos del automóvil {count}: {auto}.")
        count += 1


def parte_2():
    print("##---PARTE 2---##")

    print("Ingreso e impresión automática de instancias: \n")
    particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    print(particular)
    print(carga)
    print(bicicleta)
    print(motocicleta)

    print("\nComprobación de instancias: \n")
    print(
        "Motocicleta es instancia con relación a Vehículo:",
        isinstance(motocicleta, Vehiculo),
    )
    print(
        "Motocicleta es instancia con relación a Automovil:",
        isinstance(motocicleta, Automovil),
    )
    print(
        "Motocicleta es instancia con relación a Vehículo particular:",
        isinstance(motocicleta, Particular),
    )
    print(
        "Motocicleta es instancia con relación a Vehículo de Carga:",
        isinstance(motocicleta, Carga),
    )
    print(
        "Motocicleta es instancia con relación a Bicicleta:",
        isinstance(motocicleta, Bicicleta),
    )
    print(
        "Motocicleta es instancia con relación a Motocicleta:",
        isinstance(motocicleta, Motocicleta),
    )


def parte_3():
    print("##---PARTE 3---##")

    print("Ingreso y lectura de información en un archivo: \n")
    guardar_datos_csv()


particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

vehiculos = [particular, carga, bicicleta, motocicleta]


def guardar_datos_csv():
    try:
        archivo = open("vehiculo.csv", "w")
        archivo_csv = csv.writer(archivo)
        for vehiculo in vehiculos:
            archivo_csv.writerow((vehiculo.__class__, vehiculo.__dict__))
        archivo.close()
    except FileNotFoundError:
        print("No se ha encontrado el archivo vehiculos.csv")
    except Exception:
        print("Ha ocurrido un error inesperado")


def leer_datos_csv():
    lineas_autos = []
    with open("vehiculo.csv", "r") as datos:
        for linea in datos.readlines():
            lineas_autos.append(linea)
    print(lineas_autos)
    autos = list(lineas_autos)
    for auto in autos:
        info = auto.split(",")
        print(info[1].replace("{'marca': ", ""))


leer_datos_csv()
