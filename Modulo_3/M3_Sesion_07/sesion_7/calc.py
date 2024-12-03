print("Bienvenido a la calculadora")
print("Puedes introducir x en cualquier momento para finalizar")

while True:
    num_a = input("Introduce el numero a: ")
    if num_a.lower() == "x":
        break
    num_b = input("Introduce el numero b: ")
    if num_b.lower() == "x":
        break
    operador = input("Introduce el operador (+, -, *, /: ")
    if operador.lower() == "x":
        break

    num_a = float(num_a)
    num_b = float(num_b)

    if operador == "+":
        result = num_a + num_b
        print("El resultado de la suma es:", result)
    elif operador == "-":
        result = num_a - num_b
        print("El resultado de la resta es:", result)
    elif operador == "*":
        result = num_a * num_b
        print("El resultado de la multiplicacion es:", result)
    else:
        if num_b == 0:
            print("operación invalida")
        else:
            result = num_a / num_b
            print("El resultado de la resta es:", result)
    print("--------------------------------------")

print("¡Entendido! ¡Hasta pronto!")
