from django import forms
from .models import Brand, Equipment, Model


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }


class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ["serial", "brand", "model"]
        widgets = {
            "serial": forms.TextInput(attrs={"class": "form-control"}),
            "brand": forms.Select(attrs={"class": "form-select"}),
            "model": forms.Select(attrs={"class": "form-select"}),
        }
