from django import forms
from .models import VehiculoModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = VehiculoModel
        fields = [
            "marca",
            "modelo",
            "serial_carroceria",
            "serial_motor",
            "categoria",
            "precio",
        ]


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Nombre de usuario"
        self.fields["email"].label = "Correo"
        self.fields["password1"].label = "Contraseña"
        self.fields["password2"].label = "Confirmar Contraseña"

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
