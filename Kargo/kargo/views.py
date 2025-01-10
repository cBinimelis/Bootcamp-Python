from django.shortcuts import render, redirect
from management.forms import ReservaForm


def home(request):
    return render(request, "index.html")


def reserva(request):
    if request.method == "POST":
        pass

    reserva_form = ReservaForm()
    context = {"reserva_form": reserva_form}
    return render(request, "reserva.html", context)
