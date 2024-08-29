num_a = float(input('Introduce el numero a: '))
num_b = float(input('Introduce el numero b: '))
operador = input('Introduce el operador (+, -, *, /: ')

if operador == '+':
    result = num_a + num_b
    print("El resultado de la suma es:", result)
elif operador == '-':
    result = num_a - num_b
    print("El resultado de la resta es:", result)
elif operador == '*':
    result = num_a * num_b
    print("El resultado de la multiplicacion es:", result)
else:
    if num_b == 0:
        print("operación invalida")
    else:
        result = num_a / num_b
        print("El resultado de la resta es:", result)