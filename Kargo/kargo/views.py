from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from management.forms import ReservaForm, ClienteForm
from management.models import Cliente, Reserva, Pista


def home(request):
    return render(request, "index.html")


def reserva(request):
    if request.method == "POST":
        cliente_form = ClienteForm(request.POST)
        reserva_form = ReservaForm(request.POST)

        nombre = cliente_form["nombre"].value()
        correo = cliente_form["correo"].value()
        telefono = cliente_form["telefono"].value()
        edad = cliente_form["edad"].value()

        id_pista = reserva_form["pista"].value()
        pista = Pista.objects.filter(pk=id_pista).first()
        fecha = reserva_form["fecha"].value()
        hora = reserva_form["hora"].value()
        estado = reserva_form["estado"].value()

        user = User.objects.create_user(nombre, correo, "kargopass")
        cliente = Cliente.objects.create(
            nombre=nombre, correo=correo, telefono=telefono, edad=edad, user=user
        )

        reserva = Reserva.objects.create(
            pista=pista, fecha=fecha, hora=hora, estado=estado, cliente=cliente
        )
        reserva.save()

        messages.success(request, "Reserva confirmada")

    cliente_form = ClienteForm()
    reserva_form = ReservaForm()
    context = {"reserva_form": reserva_form, "cliente_form": cliente_form}
    return render(request, "reserva.html", context)
