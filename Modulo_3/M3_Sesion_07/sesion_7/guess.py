import random

while True:
    num = random.randint(1, 10)
    tries = 1
    winner = False

    print("Juguemos a las adivinanzas, tienes 3 intentos")

    for i in range(3):
        print("Intento #", tries)
        guess = int(input("Elige un número del 1 al 10: "))
        if guess == num:
            winner = True
            break
        tries += 1

    if winner:
        print("Felicidades, has acertado! El número secreto era", num)
        next_round = input("¿Jugamos otra ronda? y/n: ")
        if next_round.lower() == "n":
            print("¡Espero volvamos a jugar pronto!")
            break
        else:
            print("Entendido ¡Vamos!")
    else:
        print("Lamentablemente has perdido")
        print("La respuesta era: ", num)
        break
