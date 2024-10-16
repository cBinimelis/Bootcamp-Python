class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

    # Getters
    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_nro_ruedas(self):
        return self._nro_ruedas

    # Setters
    def set_marca(self, marca):
        self._marca = marca

    def set_modelo(self, modelo):
        self._modelo = modelo

    def set_nro_ruedas(self, nro_ruedas):
        self._nro_ruedas = nro_ruedas

    def tipo(self):
        return


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    # Getters
    def get_velocidad(self):
        return self._velocidad

    def get_cilindrada(self):
        return self._cilindrada

    # Setters
    def set_velocidad(self, velocidad):
        self._velocidad = velocidad

    def set_cilindrada(self, cilindrada):
        self._cilindrada = cilindrada

    def tipo(self):
        return "Automovil"

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc"


class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos

    # Getters
    def get_nro_puestos(self):
        return self._nro_puestos

    # Setters
    def set_nro_puestos(self, nro_puestos):
        self._nro_puestos = nro_puestos

    def tipo(self):
        return "Particular"

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas, {self.velocidad}Km/h, {self.cilindrada} cc, Puestos {self.nro_puestos}"


class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

    # Getters
    def get_peso_carga(self):
        return self._peso_carga

    # Setters
    def set_peso_carga(self, peso_carga):
        self._peso_carga = peso_carga

    def tipo(self):
        return "Carga"

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas, {self.velocidad}Km/h, {self.cilindrada} cc, Carga {self.peso_carga} Kg"


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo_bicicleta):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo_bicicleta = tipo_bicicleta

    # Getters
    def get_tipo_bicicleta(self):
        return self._tipo_bicicleta

    # Setters
    def set_tipo_bicicleta(self, tipo_bicicleta):
        self._tipo_bicicleta = tipo_bicicleta

    def tipo(self):
        return "Bicicleta"

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

    # Getters
    def get_motor(self):
        return self._motor

    def get_cuadro(self):
        return self._cuadro

    def get_nro_radios(self):
        return self._nro_radios

    # Setters
    def set_motor(self, motor):
        self._motor = motor

    def set_cuadro(self, cuadro):
        self._cuadro = cuadro

    def set_nro_radios(self, nro_radios):
        self._nro_radios

    def tipo(self):
        return "Motocicleta"

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas, Tipo {self.tipo_bicicleta}, Motor {self.motor}, Cuadro {self.cuadro}, Nro Radios {self.nro_radios}"
