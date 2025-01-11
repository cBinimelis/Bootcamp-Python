from django import forms
from .models import Reserva, Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "correo", "telefono", "edad"]


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["pista", "fecha", "hora", "estado"]
        widgets = {
            "fecha": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
        }
