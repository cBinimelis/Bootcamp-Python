from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import VehiculoModel


# Create your views here.
def home(request):
    pass


def add(request):
    if request.method == "POST":
        vehiculo_form = VehiculoForm(request.POST)
        vehiculo_form.save()
        return redirect("home")
    else:
        vehiculo_form = VehiculoForm()
    context = {"vehiculo_form": vehiculo_form}
    return render(request, "vehiculo/form.html", context)


def list(request):
    vehiculos = VehiculoModel.objects.all()
    context = {"vehiculos": vehiculos}
    return render(request, "vehiculo/list.html", context)
