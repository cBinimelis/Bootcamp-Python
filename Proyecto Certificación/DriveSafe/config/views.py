from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

from clases.models import Alumno, Clase, DetalleClase
from clases.forms import AlumnoForm


def home(request):
    return render(request, "index.html")


def us(request):
    return render(request, "us.html")


def signup(request):
    if request.method == "POST":
        alumno_form = AlumnoForm(request.POST)

        nombre = alumno_form["nombre"].value()
        apellido = alumno_form["apellido"].value()
        correo = alumno_form["correo"].value()
        telefono = alumno_form["telefono"].value()
        tipo_licencia = alumno_form["tipo_licencia"].value()
        try:
            user = User.objects.create_user(correo, correo, "User123456")
            alumno = Alumno.objects.create(
                nombre=nombre,
                apellido=apellido,
                correo=correo,
                telefono=telefono,
                tipo_licencia=tipo_licencia,
                user=user,
            )

            clase1 = Clase.objects.create(
                nombre="Teórica I", tipo="T", descripcion="Primera clase teórica"
            )
            clase2 = Clase.objects.create(
                nombre="Práctica I", tipo="P", descripcion="Primera clase práctica"
            )
            clase3 = Clase.objects.create(
                nombre="Práctica II", tipo="P", descripcion="Segunda clase práctica"
            )

            DetalleClase.objects.create(clase=clase1, alumno=alumno)
            DetalleClase.objects.create(clase=clase2, alumno=alumno)
            DetalleClase.objects.create(clase=clase3, alumno=alumno)

            messages.success(request, f"Inscripción confirmada para {str(alumno)} ")
        except Exception:
            messages.warning(request, Exception)
    alumno_form = AlumnoForm()
    context = {"alumno_form": alumno_form}
    return render(request, "signup.html", context)
