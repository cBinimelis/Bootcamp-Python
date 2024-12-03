# Creación de una clase
class Alumno:
    def __init__(self):
        pass


class Auto:
    def __init__(self):
        pass


chevrolet_sedan = Auto()
nissan_versa = Auto()
print("chevrolet_sedan", type(chevrolet_sedan), chevrolet_sedan)
print("nissan_versa", type(nissan_versa), nissan_versa)


class Animal:
    def __init__(self):
        pass


# Instanciación de una clase
perro = Animal()
gato = Animal()

print("DOG", type(perro), perro)
print("CAT", type(gato), gato)


class Book:
    def __init__(self, title, author, year, editorial):
        self.title = title
        self.author = author
        self.year = year
        self.editorial = editorial


harry_potter = Book("Harry Popote", "JK Rowling", 1999, "Planeta")

print(harry_potter.title)


class Computer:
    def __init__(self, types, brand, ram, year):
        self.types = types
        self.brand = brand
        self.ram = ram
        self.year = year


notebook = Computer("Laptop", "Asus", 16, 2024)
mac = Computer("Laptop", "Apple", 8, 2023)
