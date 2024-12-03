def division_enteros(x, y):
    try:
        dividendo = int(x)
        divisor = int(y)
        return dividendo / divisor
    except ZeroDivisionError:
        print("El divisor no puede ser cero")
    except ValueError:
        print("Deben ser numeros enteros")
    except Exception as error:
        print("Se ha generado un error no previsto", type(error).__name__)


resultado = division_enteros(45, 0)
print(resultado)
