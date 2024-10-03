class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.movimiento = "caminando"


class Maratonista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.movimiento = "trotando"


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.movimiento = "rodando"
