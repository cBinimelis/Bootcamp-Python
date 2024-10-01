# --------------------------------- HERENCIA ---------------------------------


class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_informacion(self):
        print(f"Cargo: {self.tipo}")
        print(f"Empleado: {self.nombre}")
        print(f"Salario: {self.salario}")

    def aumentar_salario(self, porcentaje):
        self.salario = self.salario + self.salario * (porcentaje / 100)
        print(f"El salario de {self.nombre} ha sido aumentado a {self.salario}")


class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje
        self.tipo = "Desarrollador"

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Lenguaje: {self.lenguaje}")


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
        self.tipo = "Gerente"

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Departamento: {self.departamento}")

    def cambiar_departamento(self, nuevo_departamento):
        self.departamento = nuevo_departamento
        print(f"El gerente {self.nombre} cambió al departamento {self.departamento}")


class Interno(Empleado):
    def __init__(self, nombre, salario, duracion):
        super().__init__(nombre, salario)
        self.duracion = duracion
        self.tipo = "Interno"

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Duración: {self.duracion}")

    def extender_pasantia(self, nueva_duarcion):
        self.duracion = nueva_duarcion
        print(f"El interno {self.nombre} extendió su duración a {self.duracion}")


dev = Desarrollador("Sergio", 2000, "Python")
gerente = Gerente("Angela", 5000, "Ventas")
interno = Interno("Mario", 500, 3)

dev.mostrar_informacion()
print("-------------------")
gerente.mostrar_informacion()
print("-------------------")
interno.mostrar_informacion()
