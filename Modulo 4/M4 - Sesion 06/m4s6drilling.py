def print_key():
    usuarios = {"001": "Mark", "002": "Monica", "003": "Jacob"}
    id_usuario = "004"
    try:
        print(usuarios[id_usuario])
    except KeyError:
        print("La clave 004 no está en el diccionario. Añadiendo clave...")
    finally:
        usuarios[id_usuario] = "Ninguno"
        print(usuarios)


print_key()
