import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR)

try:
    numero = int(input("Dame un número"))
    operacion = 10 / numero
except ZeroDivisionError as error:
    logger.error(f"División por 0, {error}")
except ValueError as e:
    logger.error(f"Numero inválido, {e}")
finally:
    print("Instruccion Final")


# ---------------------- ERRORES PERSONALIZADOS ----------------------
class CustomError(Exception):
    pass


def llamar_error():
    raise CustomError("Error personalizado")


llamar_error()
