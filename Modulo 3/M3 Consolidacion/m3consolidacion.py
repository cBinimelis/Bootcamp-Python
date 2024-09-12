lista_famosos = [
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes",
]
lista_magos = []
lista_cientificos = []
lista_otros = []


for famoso in lista_famosos:
    if famoso == "Harry Houdini" or famoso == "David Blaine" or famoso == "Teller":
        lista_magos.append(famoso)
    elif famoso == "Newton" or famoso == "Einstein" or famoso == "Hawking":
        lista_cientificos.append(famoso)
    else:
        lista_otros.append(famoso)


def hacer_grandioso(lista_magos):
    for i in range(len(lista_magos)):
        lista_magos[i] = "El gran " + lista_magos[i]
    return lista_magos


def imprimir_nombres(lista_nombres):
    for persona in lista_nombres:
        print(persona)


imprimir_nombres(lista_famosos)
lista_magos = hacer_grandioso(lista_magos)
imprimir_nombres(lista_magos)
imprimir_nombres(lista_cientificos)
imprimir_nombres(lista_otros)
