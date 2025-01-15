from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm


# Create your views here.
def producto_list(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, "producto/list.html", context)


def producto_create(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        form.save()
        return redirect("productos:producto_list")
    else:
        form = ProductoForm()
    context = {"form": form}
    return render(request, "producto/form.html", context)
