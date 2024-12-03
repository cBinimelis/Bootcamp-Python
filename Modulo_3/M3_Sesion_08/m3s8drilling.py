lista = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]
diccionario = dict()

for collection in lista:
    if collection[0] == 0:
        continue
    for item in collection:
        if item == 0:
            continue
        else:
            print(item)

diccionario["A"] = lista[0]
diccionario["B"] = lista[1]
diccionario["C"] = lista[2]
diccionario["D"] = lista[3]
print(diccionario)
