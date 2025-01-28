from django.shortcuts import render, redirect
from .models import Laboratorio
from .forms import LaboratorioForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import connection


# Create your views here.


# LABORATORIO ----------------------------------------------------------------
def laboratorio_list(request):
    laboratorios = Laboratorio.objects.all()
    context = {"laboratorios": laboratorios}
    return render(request, "laboratorio/laboratorio/list.html", context)


def laboratorio_create(request):
    if request.method == "POST":
        form = LaboratorioForm(request.POST)
        form.save()
        return redirect("laboratorio:laboratorio_list")
    else:
        form = LaboratorioForm()
    context = {"form": form}
    return render(request, "laboratorio/laboratorio/form.html", context)


def laboratorio_edit(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    if request.method == "POST":
        form = LaboratorioForm(request.POST, instance=laboratorio)
        form.save()
        return redirect("laboratorio:laboratorio_list")
    else:
        form = LaboratorioForm(instance=laboratorio)
    context = {"form": form}
    return render(request, "laboratorio/laboratorio/form.html", context)


def laboratorio_delete(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    if request.method == "POST":
        laboratorio.delete()
        return redirect("laboratorio:laboratorio_list")
    else:
        context = {"laboratorio": laboratorio}
        return render(request, "laboratorio/laboratorio/confirm_delete.html", context)


def laboratorio_view(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    context = {"laboratorio": laboratorio}
    return render(request, "laboratorio/laboratorio/view.html", context)
