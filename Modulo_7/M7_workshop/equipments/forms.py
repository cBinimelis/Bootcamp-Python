from django import forms
from .models import Brand, Equipment


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ["name"]


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ["serial", "brand", "model"]
        widgets = {
            "serial": forms.TextInput(),
            "brand": forms.Select(),
            "model": forms.Select(),
        }
