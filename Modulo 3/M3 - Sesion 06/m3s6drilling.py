num_a = int(input("Introduzca el numero a: "))
num_b = int(input("Introduzca el numero b: "))
num_c = int(input("Introduzca el numero c: "))

if num_a > num_b:
    if num_a > num_c:
        if num_b > num_c:
            print(num_a, num_b, num_c)
        else:
            print(num_a, num_c, num_b)
    else:
        print(num_c, num_a, num_b)
else:
    if num_b > num_c:
        if num_a > num_c:
            print(num_b, num_a, num_c)
        else:
            print(num_b, num_c, num_a)
    else:
        print(num_c, num_b, num_a)
