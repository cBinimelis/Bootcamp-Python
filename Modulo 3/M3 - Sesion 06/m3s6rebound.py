number = int(input("Ingresa un numero: "))
if number == 0:
    print("El numero es 0")
elif number % 2 == 0:
    if number < 0:
        print("El numero es negativo y par.")
    else:
        print("El numero es positivo y par.")
else:
    if number < 0:
        print("El numero es negativo e inpar.")
    else:
        print("El numero es positivo e inpar.")
