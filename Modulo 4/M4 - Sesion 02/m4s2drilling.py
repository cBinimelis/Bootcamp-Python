class Person:
    def __init__(self, nombre, apellidos, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre


persona_1 = Person("Pedro", "Vivas", "Masculino", 20, 1.78, 68)
persona_2 = Person("Juan", "Camargo", "Masculino", 18, 1.8, 75)
