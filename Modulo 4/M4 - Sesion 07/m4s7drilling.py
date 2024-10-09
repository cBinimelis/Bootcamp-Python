class RangoSalarioError(Exception):
    def __init__(
        self, salario, mensaje="El salario no se encuentra en el rango de 1000 a 2000"
    ):
        self.salario = salario
        self.mensaje = mensaje
        super().__init__(self.mensaje)


def obtener_salario():
    while True:
        try:
            salario = int(input("Por favor, ingresa tu salario: "))
            if 1000 <= salario <= 2000:
                return salario
            else:
                raise RangoSalarioError(salario)
        except ValueError:
            print("Salario no válido. Inténtalo de nuevo.")
        except RangoSalarioError as error:
            print(error)


salario = obtener_salario()
print(f"El salario ingresado es: {salario}")
