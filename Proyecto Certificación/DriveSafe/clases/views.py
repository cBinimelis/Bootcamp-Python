from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from time import strftime

from .models import Alumno, Instructor, Clase, Vehiculo, DetalleClase
from .forms import AlumnoForm, InstructorForm, ClaseForm, VehiculoForm, DetalleClaseForm

# from .forms import PistaForm
from django.db import connection


# Create your views here.
@login_required
def home(request):
    user = obtener_usuario(request)
    # query = """
    # SELECT * FROM management_pista
    # """
    # data = execute_sql(query)
    context = {"user": user}
    return render(request, "clases/index.html", context)


def obtener_usuario(request):
    if request.user.is_superuser:
        return request.user
    elif request.user.is_staff:
        user = Instructor.objects.get(correo=request.user)
        return user
    else:
        user = Alumno.objects.get(correo=request.user)
        return user


def execute_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)

        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

        return [dict(zip(columns, row)) for row in rows]


# ALUMNOS ----------------------------------------------------------------
@login_required
def alumno_list(request):
    if request.user.is_superuser:
        alumnos = Alumno.objects.all()
        context = {"alumnos": alumnos}
        return render(request, "clases/alumnos/list.html", context)
    else:
        return redirect("clases:home")


@login_required
def alumno_create(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = AlumnoForm(request.POST)

            nombre = form["nombre"].value()
            apellido = form["apellido"].value()
            correo = form["correo"].value()
            telefono = form["telefono"].value()
            tipo_licencia = form["tipo_licencia"].value()
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

                messages.success(request, f"Alumno {str(alumno)} creado exitosamente.")
                return redirect("clases:alumno_list")
            except Exception:
                messages.warning(request, Exception)
        form = AlumnoForm()
        context = {"form": form}
        return render(request, "clases/alumnos/form.html", context)
    else:
        return redirect("clases:home")


@login_required
def alumno_edit(request, pk):
    if request.user.is_superuser:
        alumno = Alumno.objects.get(id=pk)
        user = User.objects.get(username=alumno.correo)
        if request.method == "POST":
            form = AlumnoForm(request.POST, instance=alumno)
            form.save()
            user.username = form["correo"].value()
            user.save()
            messages.success(
                request, f"Se ha actualizado al alumno {str(alumno)} exitosamente."
            )

            return redirect("clases:alumno_list")
        else:
            form = AlumnoForm(instance=alumno)
        context = {"form": form}
        return render(request, "clases/alumnos/form.html", context)
    else:
        return redirect("clases:home")


@login_required
def alumno_delete(request, pk):
    if request.user.is_superuser:
        alumno = Alumno.objects.get(id=pk)
        user = User.objects.get(username=alumno.correo)
        if request.method == "POST":
            alumno.delete()
            user.delete()
            messages.success(request, "Se ha eliminado el registro")
            return redirect("clases:alumno_list")
        else:
            context = {"alumno": alumno}
            return render(request, "clases/alumnos/confirm_delete.html", context)
    else:
        return redirect("clases:home")


@login_required
def alumno_view(request, pk):
    if request.user.is_superuser:
        alumno = Alumno.objects.get(id=pk)
        context = {"alumno": alumno}
        return render(request, "clases/alumnos/view.html", context)
    else:
        return redirect("clases:home")


# VEHICULOS ----------------------------------------------------------------
@login_required
def vehiculo_list(request):
    if request.user.is_superuser:
        vehiculos = Vehiculo.objects.all()
        context = {"vehiculos": vehiculos}
        return render(request, "clases/vehiculos/list.html", context)
    else:
        return redirect("clases:home")


@login_required
def vehiculo_create(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = VehiculoForm(request.POST)
            form.save()
            messages.success(request, "Vehiculo creado")
            return redirect("clases:vehiculo_list")
        else:
            form = VehiculoForm()
        context = {"form": form}
        return render(request, "clases/vehiculos/form.html", context)
    else:
        return redirect("clases:home")


@login_required
def vehiculo_edit(request, pk):
    if request.user.is_superuser:
        vehiculo = Vehiculo.objects.get(id=pk)
        if request.method == "POST":
            form = VehiculoForm(request.POST, instance=vehiculo)
            form.save()
            return redirect("clases:vehiculo_list")
        else:
            form = VehiculoForm(instance=vehiculo)
        context = {"form": form}
        return render(request, "clases/vehiculos/form.html", context)
    else:
        return redirect("clases:home")


@login_required
def vehiculo_delete(request, pk):
    if request.user.is_superuser:
        vehiculo = Vehiculo.objects.get(id=pk)
        if request.method == "POST":
            vehiculo.delete()
            messages.success(request, "Se ha eliminado el registro")
            return redirect("clases:vehiculo_list")
        else:
            context = {"vehiculo": vehiculo}
            return render(request, "clases/vehiculos/confirm_delete.html", context)
    else:
        return redirect("clases:home")


@login_required
def vehiculo_view(request, pk):
    if request.user.is_superuser:
        vehiculo = Vehiculo.objects.get(id=pk)
        context = {"vehiculo": vehiculo}
        return render(request, "clases/vehiculos/view.html", context)
    else:
        return redirect("clases:home")


# INSTRUCTORES ----------------------------------------------------------------
@login_required
def instructor_list(request):
    if request.user.is_superuser:
        instructores = Instructor.objects.all()
        context = {"instructores": instructores}
        return render(request, "clases/instructores/list.html", context)
    else:
        return redirect("clases:home")


@login_required
def instructor_create(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = InstructorForm(request.POST)

            nombre = form["nombre"].value()
            apellido = form["apellido"].value()
            correo = form["correo"].value()
            telefono = form["telefono"].value()
            try:
                user = User.objects.create_user(correo, correo, "User123456")
                instructor = Instructor.objects.create(
                    nombre=nombre,
                    apellido=apellido,
                    correo=correo,
                    telefono=telefono,
                    user=user,
                )

                user.is_staff = True
                user.save()

                messages.success(
                    request, f"Instructor {str(instructor)} creado exitosamente."
                )
                return redirect("clases:instructor_list")
            except Exception:
                messages.warning(request, Exception)
        form = InstructorForm()
        context = {"form": form}
        return render(request, "clases/instructores/form.html", context)
    else:
        return redirect("clases:home")


@login_required
def instructor_edit(request, pk):
    if request.user.is_superuser:
        instructor = Instructor.objects.get(id=pk)
        user = User.objects.get(username=instructor.correo)
        if request.method == "POST":
            form = InstructorForm(request.POST, instance=instructor)
            form.save()
            user.username = form["correo"].value()
            user.save()
            messages.success(
                request,
                f"Se ha actualizado al instructor {str(instructor)} exitosamente.",
            )

            return redirect("clases:instructor_list")
        else:
            form = InstructorForm(instance=instructor)
        context = {"form": form}
        return render(request, "clases/instructores/form.html", context)
    else:
        return redirect("clases:home")


@login_required
def instructor_delete(request, pk):
    if request.user.is_superuser:
        instructor = Instructor.objects.get(id=pk)
        user = User.objects.get(username=instructor.correo)
        if request.method == "POST":
            instructor.delete()
            user.delete()
            messages.success(request, "Se ha eliminado el registro")
            return redirect("clases:instructor_list")
        else:
            context = {"instructor": instructor}
            return render(request, "clases/instructores/confirm_delete.html", context)
    else:
        return redirect("clases:home")


@login_required
def instructor_view(request, pk):
    if request.user.is_superuser:
        instructor = Instructor.objects.get(id=pk)
        context = {"instructor": instructor}
        return render(request, "clases/instructores/view.html", context)
    else:
        return redirect("clases:home")


# CLASES ----------------------------------------------------------------
@login_required
def clase_list(request):
    if request.user.is_superuser:
        clases = Clase.objects.all()
        context = {"clases": clases}
        return render(request, "clases/clases/list.html", context)
    else:
        return redirect("clases:home")


@login_required
def clase_create(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = ClaseForm(request.POST)
            form.save()
            messages.success(request, "Clase creada")
            return redirect("clases:clase_list")
        else:
            form = ClaseForm()
        context = {"form": form}
        return render(request, "clases/clases/form.html", context)
    else:
        return redirect("clases:home")


@login_required
def clase_edit(request, pk):
    if request.user.is_superuser:
        clase = Clase.objects.get(id=pk)
        if request.method == "POST":
            form = ClaseForm(request.POST, instance=clase)
            form.save()
            return redirect("clases:clase_list")
        else:
            form = ClaseForm(instance=clase)
        context = {"form": form}
        return render(request, "clases/clases/form.html", context)
    else:
        return redirect("clases:home")


@login_required
def clase_delete(request, pk):
    if request.user.is_superuser:
        clase = Clase.objects.get(id=pk)
        if request.method == "POST":
            clase.delete()
            messages.success(request, "Se ha eliminado el registro")
            return redirect("clases:clase_list")
        else:
            context = {"clase": clase}
            return render(request, "clases/clases/confirm_delete.html", context)
    else:
        return redirect("clases:home")


@login_required
def clase_view(request, pk):
    if request.user.is_superuser:
        clase = Clase.objects.get(id=pk)
        context = {"clase": clase}
        return render(request, "clases/clases/view.html", context)
    else:
        return redirect("clases:home")


# DETALLES CLASES ----------------------------------------------------------------
@login_required
def detalle_clase_list(request):
    if request.user.is_superuser:
        detalle_clases = DetalleClase.objects.all().order_by("alumno")
        context = {"detalle_clases": detalle_clases}
        return render(request, "clases/detalle_clases/list.html", context)
    elif request.user.is_staff:
        instructor = Instructor.objects.get(correo=request.user)
        detalle_clases = DetalleClase.objects.filter(instructor=instructor).order_by(
            "alumno"
        )
        context = {"detalle_clases": detalle_clases}
        return render(request, "clases/detalle_clases/list.html", context)
    else:
        alumno = Alumno.objects.get(correo=request.user)
        detalle_clases = DetalleClase.objects.filter(alumno=alumno).order_by("estado")
        context = {"detalle_clases": detalle_clases}
        return render(request, "clases/detalle_clases/list.html", context)


@login_required
def detalle_clase_create(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form_clase = ClaseForm(request.POST)
            form_detalle = DetalleClaseForm(request.POST)

            nombre = form_clase["nombre"].value()
            tipo = form_clase["tipo"].value()
            descripcion = form_clase["descripcion"].value()

            alumno_id = form_detalle["alumno"].value()
            alumno = Alumno.objects.get(id=alumno_id)
            instructor_id = form_detalle["instructor"].value()
            instructor = Instructor.objects.get(id=instructor_id)
            vehiculo_id = form_detalle["vehiculo"].value()
            vehiculo = Vehiculo.objects.get(id=vehiculo_id)
            estado = form_detalle["estado"].value()
            resultado = form_detalle["resultado"].value()

            clase = Clase.objects.create(
                nombre=nombre, tipo=tipo, descripcion=descripcion
            )

            DetalleClase.objects.create(
                clase=clase,
                alumno=alumno,
                instructor=instructor,
                vehiculo=vehiculo,
                estado=estado,
                resultado=resultado,
            )

            messages.success(request, "Clase creada exitosamente")
            return redirect("clases:detalle_clase_list")
        else:
            form_clase = ClaseForm()
            form_detalle = DetalleClaseForm()
        context = {"form_detalle": form_detalle, "form_clase": form_clase}
        return render(request, "clases/detalle_clases/form.html", context)
    else:
        return redirect("clases:home")


@login_required
def detalle_clase_edit(request, pk):
    if request.user.is_superuser:
        detalle_clase = DetalleClase.objects.get(id=pk)
        if request.method == "POST":
            if request.POST["estado"] == "P":
                form = DetalleClaseForm(request.POST, instance=detalle_clase)
                form.save()

                detalle_clase = DetalleClase.objects.get(id=pk)
                print(detalle_clase)
                detalle_clase.estado = "E"
                detalle_clase.hora = strftime("%H:%M:%S")
                detalle_clase.fecha = strftime("%Y-%m-%d")
                detalle_clase.save()
            else:
                form = DetalleClaseForm(request.POST, instance=detalle_clase)
                form.save()

            return redirect("clases:detalle_clase_list")
        else:
            form = DetalleClaseForm(instance=detalle_clase)
        context = {"form": form}
        return render(request, "clases/detalle_clases/form.html", context)
    else:
        return redirect("clases:home")


@login_required
def detalle_clase_delete(request, pk):
    if request.user.is_superuser:
        detalle_clase = DetalleClase.objects.get(id=pk)
        if request.method == "POST":
            detalle_clase.delete()
            messages.success(request, "Se ha eliminado el registro")
            return redirect("clases:detalle_clase_list")
        else:
            context = {"detalle_clase": detalle_clase}
            return render(request, "clases/detalle_clases/confirm_delete.html", context)
    else:
        return redirect("clases:home")


@login_required
def detalle_clase_view(request, pk):
    detalle_clase = DetalleClase.objects.get(id=pk)
    context = {"detalle_clase": detalle_clase}
    return render(request, "clases/detalle_clases/view.html", context)
