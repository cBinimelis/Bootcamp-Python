def calcular_area(base, altura):
    area = 0
    if base < 1 or altura < 1:
        print("Los valores ingresados deben ser positivos y mayores a 0")
    else:
        area = base * altura
    return area
