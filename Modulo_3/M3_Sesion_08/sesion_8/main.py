# Sin parametros y sin retorno
def saludar():
    print("Hola!")


saludar()


# Con parámetros y retorno
def mayor_que(a, b):
    if a > b:
        return a
    else:
        return


num_mayor = mayor_que(5, 5)
print(f"El numero mayor es {num_mayor}")


# Retorno de tuplas
def retupla():
    edad = 70
    isActive = False
    return (edad, isActive)


val_edad, val_active = retupla()
print(val_edad)
print(val_active)

# Recibir una nomina de trabajadores y se calculará su sueldo y bonificaciones
personal = [
    {"rut": 1, "name": "Juan", "ht": 24, "type": "Docente", "absences": 0},
    {"rut": 2, "name": "Pedro", "ht": 20, "type": "Docente", "absences": 1},
    {"rut": 3, "name": "María", "ht": 20, "type": "Auxiliar", "absences": 0},
]


def salary(persona):
    salary = 0
    bonus = 0
    match persona["type"]:
        case "Docente":
            salary = persona["ht"] * 0.6 * 18
            if persona["absences"] == 0:
                bonus = salary * 0.10
            else:
                bonus = salary * 0.05
        case "Auxiliar":
            salary = persona["ht"] * 0.4 * 15
            if persona["absences"] == 0:
                bonus = salary * 0.10
            else:
                bonus = salary * 0.05

    return salary, bonus


for worker in personal:
    w_salary, w_bonus = salary(worker)
    print(f"Rut: {worker['rut']}, salario: {w_salary}, bonus: {w_bonus}")

# Diccionario como parámetro
{""}


def get_productos(**productos):
    for codigo, descripcion in productos.items():
        print(codigo)
        print(descripcion)
