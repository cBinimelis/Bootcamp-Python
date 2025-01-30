from django.urls import path
from . import views

app_name = "clases"

urlpatterns = [
    path("", views.home, name="home"),
    # ALUMNOS-------------------------------------------------------------------
    path("alumnos/", views.alumno_list, name="alumno_list"),
    path("alumnos/create/", views.alumno_create, name="alumno_create"),
    path("alumnos/<int:pk>/edit", views.alumno_edit, name="alumno_edit"),
    path("alumnos/<int:pk>/delete", views.alumno_delete, name="alumno_delete"),
    path("alumnos/<int:pk>", views.alumno_view, name="alumno_view"),
    # VEHICULOS-------------------------------------------------------------------
    path("vehiculos/", views.vehiculo_list, name="vehiculo_list"),
    path("vehiculos/create/", views.vehiculo_create, name="vehiculo_create"),
    path("vehiculos/<int:pk>/edit", views.vehiculo_edit, name="vehiculo_edit"),
    path("vehiculos/<int:pk>/delete", views.vehiculo_delete, name="vehiculo_delete"),
    path("vehiculos/<int:pk>", views.vehiculo_view, name="vehiculo_view"),
    # CLASES-------------------------------------------------------------------
    path("clases/", views.clase_list, name="clase_list"),
    path("clases/create/", views.clase_create, name="clase_create"),
    path("clases/<int:pk>/edit", views.clase_edit, name="clase_edit"),
    path("clases/<int:pk>/delete", views.clase_delete, name="clase_delete"),
    path("clases/<int:pk>", views.clase_view, name="clase_view"),
    # INSTRUCTORES-------------------------------------------------------------------
    path("instructores/", views.instructor_list, name="instructor_list"),
    path("instructores/create/", views.instructor_create, name="instructor_create"),
    path("instructores/<int:pk>/edit", views.instructor_edit, name="instructor_edit"),
    path(
        "instructores/<int:pk>/delete",
        views.instructor_delete,
        name="instructor_delete",
    ),
    path("instructores/<int:pk>", views.instructor_view, name="instructor_view"),
    # DETALLE CLASES-------------------------------------------------------------------
    path("detalle-clases/", views.detalle_clase_list, name="detalle_clase_list"),
    path(
        "detalle-clases/create/",
        views.detalle_clase_create,
        name="detalle_clase_create",
    ),
    path(
        "detalle-clases/<int:pk>/edit",
        views.detalle_clase_edit,
        name="detalle_clase_edit",
    ),
    path(
        "detalle-clases/<int:pk>/delete",
        views.detalle_clase_delete,
        name="detalle_clase_delete",
    ),
    path(
        "detalle-clases/<int:pk>", views.detalle_clase_view, name="detalle_clase_view"
    ),
]
