rangoA = range(4)
print(rangoA, list(rangoA))

rangoB = range(2, 6)
print(rangoB, list(rangoB))

rangoC = range(1, 10, 3)
print(rangoC, list(rangoC))

print('***********************')

for index in rangoC:
    print(index)

print('bloque principal 1')

alumnos = ["Juan", "Pedro", "Diego"]
for alumno in alumnos:
    print(f"El alumnos es: {alumno}")

notas = [
    {"nombre": "Juan", "nota": 7},
    {"nombre": "Maria", "nota": 7}
]
for alumno in notas:
    print(f"{alumno['nombre']} su nota {alumno['nota']}")
