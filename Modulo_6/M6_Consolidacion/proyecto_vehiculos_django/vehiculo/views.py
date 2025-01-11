from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import VehiculoModel


# Create your views here.
def home(request):
    pass


def add(request):
    if request.user.has_perm("vehiculo.add_vehiculomodel"):
        if request.method == "POST":
            vehiculo_form = VehiculoForm(request.POST)
            vehiculo_form.save()
            return redirect("home")
        else:
            vehiculo_form = VehiculoForm()
        context = {"vehiculo_form": vehiculo_form}
        return render(request, "vehiculo/form.html", context)
    return redirect("vehiculo:list")


def list(request):
    if request.user.has_perm("vehiculo.visualizar_catalogo"):
        vehiculos = VehiculoModel.objects.all()
        for vehiculo in vehiculos:
            setattr(vehiculo, "condicion", str(vehiculo).split("-")[2])
    else:
        vehiculos = ""
    context = {"vehiculos": vehiculos}
    return render(request, "vehiculo/list.html", context)
