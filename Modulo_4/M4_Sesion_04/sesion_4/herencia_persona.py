class Persona:
    def __init__(self, nombre, apellidos, cedula):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cedula = cedula

    def imprimir_datos(self):
        print(
            f"Nombre: {self.nombre} \nApellidos: {self.apellidos} \nCédula: {self.cedula}"
        )

    def get_tipo(self):
        print("Soy del tipo Persona")

    def __str__(self):
        return f"Nombre: {self.nombre} \nApellidos: {self.apellidos} \nCédula: {self.cedula}"


persona1 = Persona("Juan", "Perez", "123456")
persona2 = Persona("José", "Sanchez", "456789")

persona1.imprimir_datos()
print(persona1)

persona2.imprimir_datos()
print(persona2)


print("-----------------------------------------------------------------")


class Supervisor(Persona):
    def __init__(self, nombre, apellidos, cedula, zona):
        super().__init__(nombre, apellidos, cedula)
        self.zona = zona

    def imprimir_supervisor(self):
        super().imprimir_datos()
        print(f"Zona: {self.zona}")

    def get_tipo(self):
        print("Soy del tipo Supervisor")

    def __str__(self):
        return super().__str__() + f"\nZona: {self.zona}"


class Cliente(Persona):
    def __init__(self, nombre, apellidos, cedula, descuento):
        super().__init__(nombre, apellidos, cedula)
        self.descuento = descuento

    def imprimir_cliente(self):
        super().imprimir_datos()
        print("Descuento: ", self.descuento)

    def get_tipo(self):
        print("Soy del tipo Cliente")

    def __str__(self):
        return super().__str__() + f" \nDescuento: {self.descuento}"


supervisor1 = Supervisor("Juan", "Perez", "123456", "Sur")
print("******")
supervisor1.imprimir_datos()
print("******")
supervisor1.imprimir_supervisor()
print("******")
print(supervisor1)

cliente1 = Cliente("Juan", "Perez", "123456", 20)
print("******")
cliente1.imprimir_datos()
print("******")
cliente1.imprimir_cliente()
print("******")
print(cliente1)


print("******")
persona1 = Persona("Juan", "Perez", "123456")
persona1.get_tipo()

print("******")
supervisor1 = Supervisor("Juan", "Perez", "123456", "Sur")
supervisor1.get_tipo()

print("******")
cliente1 = Cliente("Juan", "Perez", "123456", 20)
cliente1.get_tipo()
