import matematicas.aritmetica
from matematicas import  geometria

print(matematicas.aritmetica.sumar(34,534))

print(geometria.area_circle(12))

print('-----Listas-----')

students = ["Patricio", "Sofía", "Helena"]
notes = list()

students.append("Charles")
notes.append(7)
notes.append(5)

notes.insert(1,4)

students.extend(["Carlos","Pepe", "José"])

print(type(students), students)
print(type(notes), notes)


print('-----Tuplas-----')
codigo_postal=(4440000, "Los Angeles")

print(type(codigo_postal), codigo_postal)