from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def palindromo(request, palabra):
    resultado = comprobar_palindromo(palabra)
    context = {"resultado": resultado}
    return render(request, "palindromo.html", context)


def comprobar_palindromo(palabra):
    palabra_base = palabra.replace(" ", "")
    r_palabra = list(palabra_base)
    r_palabra.reverse()
    if r_palabra == list(palabra_base):
        return f"{palabra} es palíndromo"
    else:
        return f"{palabra} no es palíndromo"
