##############################################################
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 3 ###
class Restaurante:
    def __init__(self, nombre, platos, cocineros, repartidores):
        self.nombre = nombre
        self.platos = platos
        self.cocineros = cocineros
        self.repartidores = repartidores
        self.calificacion = 0

    def recibir_pedidos(self, clientes):
        total_calificaciones = 0
        for cliente in clientes:
            pedido = []
            for plato_cliente in cliente.platos_preferidos:
                if plato_cliente in self.platos:
                    nombre_plato, tipo_plato = self.platos[plato_cliente]
                    cocinero_disponible = None
                    for cocinero in self.cocineros:
                        if cocinero.energia > 0:
                            cocinero_disponible = cocinero
                            break
                    if cocinero_disponible:
                        plato_listo = cocinero_disponible.cocinar(
                            [nombre_plato, tipo_plato]
                        )
                        pedido.append(plato_listo)

            repartidor_disponible = None
            demora = 0
            for repartidor in self.repartidores:
                if repartidor.energia > 0:
                    repartidor_disponible = repartidor
                    break
            if repartidor_disponible:
                demora = repartidor_disponible.repartir(pedido)
            else:
                pedido = []
                demora = 0

            calificacion_cliente = cliente.recibir_pedido(pedido, demora)
            total_calificaciones += calificacion_cliente

        self.calificacion = total_calificaciones / len(clientes)


### FIN PARTE 3 #


if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
            "Pepsi": ["Pepsi", "Bebestible"],
            "Mariscos": ["Mariscos", "Comestible"],
        }
        un_restaurante = Restaurante("Bon Appetit", PLATOS_PRUEBA, [], [])
        print(f"El restaurante {un_restaurante.nombre}, tiene los siguientes platos:")
        for plato in un_restaurante.platos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print(
            "Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase"
        )
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
