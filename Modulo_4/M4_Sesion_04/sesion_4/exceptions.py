import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR)

try:
    a = 0
    b = 1 / a
except ZeroDivisionError as error:
    logger.error(f"Division por 0; {error}")
    print("No se puede dividir por cero")

print("Cuerpo principal del código")

try:
    edad = int(input("Introduce  tu edad: "))
except ValueError as error:
    logger.error(f"Valor no aceptable: {error}")
