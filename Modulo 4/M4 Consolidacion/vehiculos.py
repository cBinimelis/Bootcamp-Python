class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc"


class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puesto):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puesto = nro_puesto

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas, {self.velocidad}Km/h, {self.cilindrada} cc, Puestos {self.nro_puesto}"


class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas, {self.velocidad}Km/h, {self.cilindrada} cc, Carga {self.peso_carga} Kg"


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo_bicicleta):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo_bicicleta = tipo_bicicleta

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas, Tipo {self.tipo_bicicleta}"


class Motocicleta(Bicicleta):
    def __init__(
        self, marca, modelo, nro_ruedas, tipo_bicicleta, motor, cuadro, nro_radios
    ):
        super().__init__(marca, modelo, nro_ruedas, tipo_bicicleta)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas, Tipo {self.tipo_bicicleta}, Motor {self.motor}, Cuadro {self.cuadro}, Nro Radios {self.nro_radios}"
