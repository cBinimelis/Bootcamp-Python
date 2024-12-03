conjunto_a = set()
conjunto_b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(type(conjunto_a), conjunto_a)
print(type(conjunto_b), conjunto_b)

conjunto = {1, 3, 5, 7, 9}
print(conjunto)
conjunto.add(-1)
print(conjunto)
conjunto.remove(5)
print(conjunto)
conjunto.discard(13)
print(conjunto)
conjunto.discard(7)
print(conjunto)

conjunto_a.add("A")
conjunto_a.add("B")
conjunto_a.add("C")
conjunto_a.add(2)
conjunto_a.add(4)
conjunto_a.add(6)
conjunto_a.add(8)

conjunto_c = conjunto_a | conjunto_b
print("Union de conjuntos: ", conjunto_c)

# Ignorado
conjunto_c.add("A")
print("Ignorado: ", conjunto_c)

# Añadido
conjunto_c.add("a")
print("Agregado: ", conjunto_c)

conjunto_d = conjunto_a & conjunto_b
print("Intersección de conjuntos: ", conjunto_d)

conjunto_e = conjunto_a - conjunto_b
print("Diferencia de conjuntos: ", conjunto_e)

conjunto_f = conjunto_a ^ conjunto_b
print("Diferencia Simetrica de conjuntos: ", conjunto_f)