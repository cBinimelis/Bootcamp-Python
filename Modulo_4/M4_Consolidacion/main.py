from vehiculos import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta
import csv


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

    print("\n--------------------------------------------------\n")


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

    print("\n--------------------------------------------------\n")


def parte_3():
    print("##---PARTE 3---##")

    print("Ingreso y lectura de información en un archivo: \n")
    print("Guardando datos...")

    guardar_datos_csv()

    print("¡Datos guardados existosamente!\n")
    print("\nLeyendo datos: ")

    leer_datos_csv()

    print("¡Datos leídos exitosamente!")

    print("\n--------------------------------------------------\n")


particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

vehiculos = [particular, carga, bicicleta, motocicleta]


def guardar_datos_csv():
    try:
        with open("vehiculo.csv", "w", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(
                [
                    "tipo",
                    "marca",
                    "modelo",
                    "nro_ruedas",
                    "velocidad",
                    "cilindrada",
                    "nro_puestos",
                    "peso_carga",
                    "tipo_bicicleta",
                    "motor",
                    "cuadro",
                    "nro_radios",
                ]
            )
            for vehiculo in vehiculos:
                if isinstance(vehiculo, Motocicleta):
                    escritor.writerow(
                        [
                            vehiculo.tipo(),
                            vehiculo.marca,
                            vehiculo.modelo,
                            vehiculo.nro_ruedas,
                            "",
                            "",
                            "",
                            "",
                            vehiculo.tipo_bicicleta,
                            vehiculo.motor,
                            vehiculo.cuadro,
                            vehiculo.nro_radios,
                        ]
                    )
                elif isinstance(vehiculo, Bicicleta):
                    escritor.writerow(
                        [
                            vehiculo.tipo(),
                            vehiculo.marca,
                            vehiculo.modelo,
                            vehiculo.nro_ruedas,
                            "",
                            "",
                            "",
                            "",
                            vehiculo.tipo_bicicleta,
                            "",
                            "",
                            "",
                        ]
                    )

                elif isinstance(vehiculo, Carga):
                    escritor.writerow(
                        [
                            vehiculo.tipo(),
                            vehiculo.marca,
                            vehiculo.modelo,
                            vehiculo.nro_ruedas,
                            vehiculo.velocidad,
                            vehiculo.cilindrada,
                            "",
                            vehiculo.peso_carga,
                            "",
                            "",
                            "",
                            "",
                        ]
                    )

                elif isinstance(vehiculo, Particular):
                    escritor.writerow(
                        [
                            vehiculo.tipo(),
                            vehiculo.marca,
                            vehiculo.modelo,
                            vehiculo.nro_ruedas,
                            vehiculo.velocidad,
                            vehiculo.cilindrada,
                            vehiculo.nro_puestos,
                            "",
                            "",
                            "",
                            "",
                            "",
                        ]
                    )

                elif isinstance(vehiculo, Automovil):
                    escritor.writerow(
                        [
                            vehiculo.tipo(),
                            vehiculo.marca,
                            vehiculo.modelo,
                            vehiculo.nro_ruedas,
                            vehiculo.velocidad,
                            vehiculo.cilindrada,
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                        ]
                    )
    except FileNotFoundError:
        print("No se ha encontrado el archivo vehiculos.csv")
    except Exception:
        print("Ha ocurrido un error inesperado")


def leer_datos_csv():
    automoviles = []
    particulares = []
    cargas = []
    bicicletas = []
    motocicletas = []
    with open("vehiculo.csv", "r") as archivo:
        try:
            lector = csv.DictReader(archivo)
            for fila in lector:
                tipo = fila["tipo"]
                if tipo == "Motocicleta":
                    vehiculo = Motocicleta(
                        fila["marca"],
                        fila["modelo"],
                        fila["nro_ruedas"],
                        fila["tipo_bicicleta"],
                        fila["motor"],
                        fila["cuadro"],
                        fila["nro_radios"],
                    )
                    motocicletas.append(vehiculo)
                elif tipo == "Bicicleta":
                    vehiculo = Bicicleta(
                        fila["marca"],
                        fila["modelo"],
                        fila["nro_ruedas"],
                        fila["tipo_bicicleta"],
                    )
                    bicicletas.append(vehiculo)
                elif tipo == "Carga":
                    vehiculo = Carga(
                        fila["marca"],
                        fila["modelo"],
                        fila["nro_ruedas"],
                        fila["velocidad"],
                        fila["cilindrada"],
                        fila["peso_carga"],
                    )
                    cargas.append(vehiculo)
                elif tipo == "Particular":
                    vehiculo = Particular(
                        fila["marca"],
                        fila["modelo"],
                        fila["nro_ruedas"],
                        fila["velocidad"],
                        fila["cilindrada"],
                        fila["nro_puestos"],
                    )
                    particulares.append(vehiculo)
                elif tipo == "Automovil":
                    vehiculo = Automovil(
                        fila["marca"],
                        fila["modelo"],
                        fila["nro_ruedas"],
                        fila["velocidad"],
                        fila["cilindrada"],
                    )
                    automoviles.append(vehiculo)

            print("\nListado de Automoviles:")
            imprimir_listado(automoviles)
            print("\nListado de Vehiculos Particulares:")
            imprimir_listado(particulares)
            print("\nListado de Vehiculos de Carga:")
            imprimir_listado(cargas)
            print("\nListado de Bicicletas:")
            imprimir_listado(bicicletas)
            print("\nListado de Motocicletas: ")
            imprimir_listado(motocicletas)

        except FileNotFoundError:
            print("No se ha encontrado el archivo vehiculo.csv")
        except Exception as error:
            print("Ha ocurrido un error inesperado:", error)


def imprimir_listado(listado):
    for elemento in listado:
        if elemento != "None":
            print(elemento)


def iniciar_menu(funcionando):

    print("##### BIENVENIDO AL SISTEMA DE CONTROL DE VEHÍCULOS #####")
    print("")

    while funcionando:
        print("##   Selecciona una opcion  ##")
        print("I   .- Parte 1 ")
        print("II  .- Parte 2")
        print("III .- Parte 3")
        print("IV  .- Salir")
        try:
            seleccion = int(input("¿Cuál es tu elección?: "))

            match seleccion:
                case 1:
                    parte_1()
                case 2:
                    parte_2()
                case 3:
                    parte_3()
                case 4:
                    print("##### NOS VEMOS PRONTO #####")
                    funcionando = False
                case _:
                    print("Opción no válida")

        except ValueError:
            print("Has ingresado un valor no admitido.\n")
        except Exception as error:
            print("Ha ocurrido un error no previsto: ", error)


iniciar_menu(True)
