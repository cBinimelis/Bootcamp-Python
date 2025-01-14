from django.shortcuts import render, redirect
from .models import Reserva, Pista, Cliente
from .forms import ReservaForm, PistaForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import connection


# Create your views here.
@login_required
def home(request):
    query = """
    SELECT * FROM management_pista
    """
    data = execute_sql(query)
    context = {"data": data}
    return render(request, "management/index.html", context)


def execute_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)

        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

        return [dict(zip(columns, row)) for row in rows]


@login_required
def reserva_list(request):
    if request.user.is_staff:
        reservas = Reserva.objects.all()
        context = {"reservas": reservas}
        return render(request, "management/reserva/reserva_list.html", context)
    else:
        cliente = Cliente.objects.filter(user_id=request.user.id).first()
        reservas = Reserva.objects.filter(cliente_id=cliente.id)
        context = {"reservas": reservas}
        return render(request, "management/reserva/reserva_list.html", context)


@login_required
def reserva_create(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)

        id_pista = form["pista"].value()
        pista = Pista.objects.filter(pk=id_pista).first()
        fecha = form["fecha"].value()
        hora = form["hora"].value()
        estado = form["estado"].value()

        cliente = Cliente.objects.filter(user_id=request.user.id)

        reserva = Reserva.objects.create(
            pista=pista, fecha=fecha, hora=hora, estado=estado, cliente=cliente
        )
        reserva.save()
        messages.success(request, "Reserva creada")
        return redirect("management:reserva_list")
    else:
        form = ReservaForm()
    context = {"form": form}
    return render(request, "management/reserva/reserva_form.html", context)


@login_required
def reserva_edit(request, pk):
    reserva = Reserva.objects.get(id=pk)
    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        form.save()
        return redirect("management:reserva_list")
    else:
        form = ReservaForm(instance=reserva)
    context = {"form": form}
    return render(request, "management/reserva/reserva_form.html", context)


@login_required
def reserva_delete(request):
    pass


@login_required
def reserva_view(request):
    pass


@login_required  # PISTAS ----------------------------------------------------------------
def pista_list(request):
    pistas = Pista.objects.all()
    context = {"pistas": pistas}
    return render(request, "management/pista/pista_list.html", context)


@login_required
def pista_create(request):
    if request.method == "POST":
        form = PistaForm(request.POST)
        form.save()
        messages.success(request, "Pista creada")
        return redirect("management:pista_list")
    else:
        form = PistaForm()
    context = {"form": form}
    return render(request, "management/pista/pista_form.html", context)


@login_required
def pista_edit(request, pk):
    pista = Pista.objects.get(id=pk)
    if request.method == "POST":
        form = PistaForm(request.POST, instance=pista)
        form.save()
        return redirect("management:pista_list")
    else:
        form = PistaForm(instance=pista)
    context = {"form": form}
    return render(request, "management/pista/pista_form.html", context)


@login_required
def pista_delete(request, pk):
    pista = Pista.objects.get(id=pk)
    if request.method == "POST":
        pista.delete()
        return redirect("management:pista_list")
    else:
        context = {"pista": pista}
        return render(request, "management/pista/pista_confirm_delete.html", context)


@login_required
def pista_view(request, pk):
    pista = Pista.objects.get(id=pk)
    context = {"pista": pista}
    return render(request, "management/pista/pista_view.html", context)
