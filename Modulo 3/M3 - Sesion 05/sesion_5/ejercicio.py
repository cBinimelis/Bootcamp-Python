#Crear conjunto
conjunto_c = {1, 2, 3, 4, 5}
print("Conjunto C: ", conjunto_c)

# Checkear si existe 3
if (3 in conjunto_c):
    print("3 si pertenece al conjunto!")

# Eliminar 4
conjunto_c.discard(4)
print("Eliminamos el N° 4: ", conjunto_c)

# Agregar 6
conjunto_c.add(6)
print("Añadimos el N° 6: ", conjunto_c)

# Copiar C en D y luego limpiarlo
conjunto_d = conjunto_c.copy()
conjunto_c.clear()
print("Conjunto C: ", conjunto_c)
print("Conjunto D: ", conjunto_d)


#--------------------------------------------------------------
stock = ["Peras", "Manzanas", "Uvas"]
vendidos = ["Peras","Peras","Peras","Uvas","Uvas","Uvas","Limon","Limon","Limon"]

stock_list = set(stock)
vendidos_list = set(vendidos)

sin_stock= vendidos_list - stock_list
print(sin_stock)