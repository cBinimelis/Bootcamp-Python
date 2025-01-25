from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "precio", "f_vencimiento"]

        widgets = {
            "nombre": forms.TextInput(attrs={"placeholder": "Nombre del Producto"}),
            "precio": forms.NumberInput(attrs={"placeholder": "Precio del Producto"}),
            "descripcion": forms.TextInput(
                attrs={"placeholder": "Descripción del Producto"}
            ),
            "f_vencimiento": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
        }
