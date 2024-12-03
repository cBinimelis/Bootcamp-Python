estudiantes = [
    {"nombre": "Juan", "edad": 17, "calificaciones": [85, 90, 88]},
    {"nombre": "María", "edad": 19, "calificaciones": [92, 89, 90]},
    {"nombre": "Pedro", "edad": 21, "calificaciones": [85, 95, 80]},
    {"nombre": "Ana", "edad": 18, "calificaciones": [90, 92, 87]},
    {"nombre": "Luis", "edad": 20, "calificaciones": [88, 85, 92]},
]

for estudiante in estudiantes:
    calificaciones = 0
    check = 0
    for nota in estudiante["calificaciones"]:
        calificaciones += nota

    if calificaciones / 3 > 85 and estudiante["edad"] > 18:
        print(estudiante["nombre"], estudiante["edad"], estudiante["calificaciones"])
        for i in range(1, estudiante["edad"] + 1):
            if estudiante["edad"] % i == 0:
                check += 1
        if check == 2:
            print(
                "El promedio de",
                estudiante["nombre"],
                "es",
                round(calificaciones / 3, 2),
            )
