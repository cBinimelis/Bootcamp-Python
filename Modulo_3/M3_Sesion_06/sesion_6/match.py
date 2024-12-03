genre = "HH"
match genre:
    case "M":
        print("Eres hombre")
    case "F":
        print("Eres mujer")

numero = 3
match numero:
    case 1|3:
        print("Esta entre el uno o tres")
    case 4|5|6:
        print("esta entre otros numeros")

num_c = -1
match num_c:
    case n if n >0:
        print("positivo")
    case n if n <0:
        print("negativo")