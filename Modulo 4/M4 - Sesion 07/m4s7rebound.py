while True:
    try:
        edad = int(input("Por favor, ingresa tu edad: "))
        break
    except ValueError:
        print("El numero debe ser un número entero. Inténtalo de nuevo.")

if edad >= 18:
    print("Eres un adulto.")
else:
    print("No eres un adulto.")
