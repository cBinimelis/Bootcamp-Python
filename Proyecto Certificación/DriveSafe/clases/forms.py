from django import forms
from .models import Alumno, Vehiculo, Clase, Instructor, DetalleClase


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ["nombre", "apellido", "correo", "telefono", "tipo_licencia"]
        widgets = {
            "tipo_licencia": forms.Select(attrs={"class": "form-select"}),
        }


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ["modelo", "patente", "transmision", "estado"]
        widgets = {
            "transmision": forms.Select(attrs={"class": "form-select"}),
            "estado": forms.Select(attrs={"class": "form-select"}),
        }


class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = ["nombre", "tipo", "descripcion"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "tipo": forms.Select(attrs={"class": "form-select"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ["nombre", "apellido", "correo", "telefono"]


class DetalleClaseForm(forms.ModelForm):
    class Meta:
        model = DetalleClase
        fields = [
            "alumno",
            "instructor",
            "vehiculo",
            "estado",
            "resultado",
        ]
        widgets = {
            "clase": forms.Select(attrs={"class": "form-select"}),
            "alumno": forms.Select(attrs={"class": "form-select"}),
            "instructor": forms.Select(attrs={"class": "form-select"}),
            "vehiculo": forms.Select(attrs={"class": "form-select"}),
            "fecha": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
            "hora": forms.Select(attrs={"class": "form-select"}),
            "estado": forms.Select(attrs={"class": "form-select"}),
            "resultado": forms.Textarea(attrs={"rows": "4", "class": "form-control"}),
        }
