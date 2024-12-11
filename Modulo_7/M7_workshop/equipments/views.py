from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Brand, Model, Equipment
from .forms import BrandForm, EquipmentForm


# Create your views here.
def brand_list(request):
    brands = Brand.objects.all()
    context = {"brands": brands}
    return render(request, "equipments/brand_list.html", context)


def brand_create(request):
    if request.method == "POST":
        form = BrandForm(request.POST)
        form.save()
        return redirect("brand_list")
    else:
        form = BrandForm()
    context = {"form": form}
    return render(request, "equipments/brand_form.html", context)


def brand_edit(request, pk):
    brand = Brand.objects.get(id=pk)
    if request.method == "POST":
        form = BrandForm(request.POST, instance=brand)
        form.save()
        return redirect("brand_list")
    else:
        form = BrandForm(instance=brand)

    context = {"form": form}
    return render(request, "equipments/brand_form.html", context)


def brand_delete(request, pk):
    brand = Brand.objects.get(id=pk)
    if request.method == "POST":
        brand.delete()
        return redirect("brand_list")
    else:
        context = {"brand": brand}
        return render(request, "equipments/brand_confirm_delete.html", context)


def equipment_list(request):
    equipments = Equipment.objects.all()
    context = {"equipments": equipments}
    return render(request, "equipments/equipment_list.html", context)


def equipment_create(request):
    if request.method == "POST":
        form = EquipmentForm(request.POST)
        form.save()
        return redirect("equipment_list")
    else:
        form = EquipmentForm()
    context = {"form": form}
    return render(request, "equipments/equipment_form.html", context)


def equipment_edit(request, pk):
    equipment = Equipment.objects.get(id=pk)
    if request.method == "POST":
        form = EquipmentForm(request.POST, instance=equipment)
        form.save()
        return redirect("equipment_list")
    else:
        form = EquipmentForm(instance=equipment)

    context = {"form": form}
    return render(request, "equipments/equipment_form.html", context)


def equipment_delete(request, pk):
    equipment = Equipment.objects.get(id=pk)
    if request.method == "POST":
        equipment.delete()
        return redirect("equipment_list")
    else:
        context = {"equipment": equipment}
        return render(request, "equipments/equipment_confirm_delete.html", context)


def equipment_view(request, pk):
    equipment = Equipment.objects.get(id=pk)
    context = {"equipment": equipment}
    return render(request, "equipments/equipment_view.html", context)
