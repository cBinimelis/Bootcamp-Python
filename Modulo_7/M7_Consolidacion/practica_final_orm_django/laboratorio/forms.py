from django import forms
from .models import Producto, Laboratorio


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "p_venta"]


class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ["nombre", "ciudad", "pais"]
