class Animal:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def info_animal(self):
        print(f"Especie: {self.especie}")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg.")


class Ave(Animal):
    def __init__(self, nombre, edad, peso, gestacion, tamanio):
        super().__init__(nombre, edad, peso)
        self.gestacion = gestacion
        self.tamanio = tamanio
        self.especie = "Ave"

    def info_animal(self):
        super().info_animal()
        print(f"Gestación: {self.gestacion} días")
        print(f"Tamaño: {self.tamanio}")

    def emigrar(self):
        print(
            "Si bien a ",
            self.nombre,
            " le encantaría emigrar,",
            "no puede hacerlo debido a que está en cuidado del Zoologico",
        )


class Reptil(Animal):
    def __init__(self, nombre, edad, peso, riesgo, habitat):
        super().__init__(nombre, edad, peso)
        self.riesgo = riesgo
        self.habitat = habitat
        self.especie = "Reptil"

    def info_animal(self):
        super().info_animal()
        print(f"Riesgo: {self.riesgo}")
        print(f"Habitat: {self.habitat}")

    def mudar_piel(self):
        print(f"{self.nombre} ha mudado su piel satisfactoriamente")


class Bovino(Animal):
    def __init__(self, nombre, edad, peso, produccion, granja_origen):
        super().__init__(nombre, edad, peso)
        self.produccion = produccion
        self.granja_origen = granja_origen
        self.especie = "Bovino"

    def info_animal(self):
        super().info_animal()
        print(f"Produccion: {self.produccion}")
        print(f"Granja de Origen: {self.granja_origen}")

    def ordeniar(self):
        print(f"Creo que {self.nombre} no se ve con ganas de eso")


avelardo = Ave("Avelardo", 10, 68, 226, "Extremadamente Grande")
rango = Reptil("Rango", 3, 0.5, "Punteria", "El Viejo Oeste")
clara = Bovino("Clara", 5, 350, "Leche", "Santa Clara")

avelardo.info_animal()
print("-------------------")
rango.info_animal()
print("-------------------")
clara.info_animal()
