from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Brand
from .forms import BrandForm


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
