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


print("-----------------------------------------------------------------")


class Capacidades:
    def __init__(self, ncertificados, rating):
        self.ncertificados = ncertificados
        self.rating = rating

    def imprimir_capacidades(self):
        print(f"N° Certificados: {self.ncertificados} \nRating: {self.rating}")

    def __str__(self):
        return f"N° de Certificados: {self.ncertificados} \nRaiting: {self.rating}"


class SupervisorZona(Supervisor, Capacidades):
    def __init__(
        self, nombre, apellidos, cedula, zona, ncertificados, rating, promedio
    ):
        Supervisor.__init__(self, nombre, apellidos, cedula, zona)
        Capacidades.__init__(self, ncertificados, rating)
        self.promedio = promedio

    def imprimir_supervisor_zona(self):
        Supervisor.imprimir_supervisor(self)
        Capacidades.imprimir_capacidades(self)
        print("Promedio: ", self.promedio)


print("******")
supervisorzona1 = SupervisorZona("Juan", "Pérez", 123456, "Sur", 8, 25, 123)
supervisorzona1.imprimir_datos()
print("******")
supervisorzona1.imprimir_supervisor()
print("******")
supervisorzona1.imprimir_supervisor_zona()


# MÉTODOS ESPECIALES ISINSTANCE() Y __MRO__.
print("******")
supervisorzona1 = SupervisorZona("Juan", "Pérez", 123456, "Sur", 8, 25, 123)
supervisor1 = Supervisor("Pedro", "Carrillo", 123456, "Norte")

print("supervisorzona1")
# Es instancia supervisorzona1 de Persona
print(isinstance(supervisorzona1, Persona))

# Es instancia supervisorzona1 de Supervisor
print(isinstance(supervisorzona1, Supervisor))

# Es instancia supervisorzona1 de SupervisorZona
print(isinstance(supervisorzona1, SupervisorZona))

print("supervisor")
# Es instancia supervisor de Persona
print(isinstance(supervisor1, Persona))

# Es instancia supervisor de Supervisor
print(isinstance(supervisor1, Supervisor))

# Es instancia supervisor de SupervisorZona
print(isinstance(supervisor1, SupervisorZona))


print("MRO\n")
print(SupervisorZona.__mro__)
print(Supervisor.__mro__)
print(Persona.__mro__)
