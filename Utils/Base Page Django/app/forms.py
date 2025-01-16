from django import forms
from .models import Reserva, Cliente, Pista, HORAS


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "correo", "telefono", "edad"]


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["pista", "fecha", "hora", "estado"]
        widgets = {
            "pista": forms.Select(attrs={"class": "form-select"}),
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
        }


class PistaForm(forms.ModelForm):
    class Meta:
        model = Pista
        fields = ["nombre", "tipo", "cantidad_vehiculos"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "tipo": forms.Select(attrs={"class": "form-select"}),
            "cantidad_vehiculos": forms.NumberInput(attrs={"class": "form-control"}),
        }
