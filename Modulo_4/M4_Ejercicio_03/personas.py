##############################################################
from random import randint
from platos import Comestible, Bebestible

## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 2.1 ###
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


### FIN PARTE 2.1 ###


### INICIO PARTE 2.2 ###
class Repartidor(Persona):
    def __init__(self, nombre, tiempo_entrega):
        super().__init__(nombre)
        self.tiempo_entrega = tiempo_entrega
        self.energia = randint(75, 100)

    def repartir(self, pedido):
        factor_tamano = 5 if len(pedido) <= 2 else 15
        self.energia -= factor_tamano

        factor_velocidad = 1.25 if len(pedido) <= 2 else 0.85
        demora_pedido = (self.tiempo_entrega * len(pedido)) / factor_velocidad

        return demora_pedido


### FIN PARTE 2.2 ###


### INICIO PARTE 2.3 ###
class Cocinero(Persona):
    def __init__(self, nombre, habilidad):
        super().__init__(nombre)
        self.habilidad = habilidad
        self.energia = randint(50, 80)

    def cocinar(self, informacion_plato):
        plato = None
        nombre_plato, tipo_plato = informacion_plato

        if tipo_plato == "Bebestible":
            plato = Bebestible(nombre_plato)
            if plato.tamano == "Pequeño":
                self.energia -= 5
            elif plato.tamano == "Mediano":
                self.energia -= 8
            elif plato.tamano == "Grande":
                self.energia -= 10
        elif tipo_plato == "Comestible":
            plato = Comestible(nombre_plato)
            self.energia -= 15

        factor_calidad = 0.7 if plato.dificultad > self.habilidad else 1.5
        plato.calidad *= factor_calidad

        return plato


### FIN PARTE 2.3 ###


### INICIO PARTE 2.4 ###
class Cliente(Persona):
    def __init__(self, nombre, platos_preferidos):
        super().__init__(nombre)
        self.platos_preferidos = platos_preferidos

    def recibir_pedido(self, pedido, demora):
        calificacion = 10
        if len(pedido) < len(self.platos_preferidos):
            calificacion /= 2
        if demora >= 20:
            calificacion /= 2

        for plato in pedido:
            if plato.calidad >= 11:
                calificacion += 1.5
            elif plato.calidad < 8:
                calificacion -= 3
            if plato.calidad < 0:
                plato.calidad = 0

        return calificacion


### FIN PARTE 2.4 ###


if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
            "Agua": ["Agua", "Bebestible"],
            "Papas Duqueza": ["Papas Duqueza", "Comestible"],
        }
        un_cocinero = Cocinero("Cristian", randint(1, 10))
        un_repartidor = Repartidor("Tomás", randint(20, 30))
        un_cliente = Cliente("Alberto", PLATOS_PRUEBA)
        print(
            f"El cocinero {un_cocinero.nombre} tiene una habilidad: {un_cocinero.habilidad}"
        )
        print(
            f"El repatidor {un_repartidor.nombre} tiene una tiempo de entrega: {un_repartidor.tiempo_entrega} seg"
        )
        print(f"El cliente {un_cliente.nombre} tiene los siguientes platos favoritos:")
        for plato in un_cliente.platos_preferidos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print(
            "Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase"
        )
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
