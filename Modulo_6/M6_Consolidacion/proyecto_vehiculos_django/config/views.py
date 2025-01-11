from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from vehiculo.models import VehiculoModel
from vehiculo.forms import RegisterForm


def home(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            content_type = ContentType.objects.get_for_model(VehiculoModel)

            visualizar_catalogo = Permission.objects.get(
                codename="visualizar_catalogo", content_type=content_type
            )

            user = register_form.save()

            user.user_permissions.add(visualizar_catalogo)
            return redirect("login")
        else:
            messages.error(request, "ERROR EN EL FORMULARIO")
    else:
        register_form = RegisterForm()

    context = {"register_form": register_form}
    return render(request, "register.html", context)
