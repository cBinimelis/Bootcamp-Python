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


def producto_edit(request, pk):
    producto = Producto.objects.get(id=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        form.save()
        return redirect("productos:producto_list")
    else:
        form = ProductoForm(instance=producto)
    context = {"form": form}
    return render(request, "producto/form.html", context)


def producto_delete(request, pk):
    producto = Producto.objects.get(id=pk)
    if request.method == "POST":
        producto.delete()
        return redirect("productos:producto_list")
    else:
        context = {"producto": producto}
        return render(request, "producto/confirm_delete.html", context)


def producto_view(request, pk):
    producto = Producto.objects.get(id=pk)
    context = {"producto": producto}
    return render(request, "producto/view.html", context)
