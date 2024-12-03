class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        self.message = "La edad es inválida, esta debería ser entre 0 y 80"
        super().__init__(self.message)


def verify_age(age):
    if age < 0 or age > 80:
        raise InvalidAgeError(age)


try:
    age = int(input("Introduce tu edad"))
    verify_age(age)
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("Debes introducir un número válido")
