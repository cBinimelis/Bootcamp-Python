from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "example@mail.com"}
        )
    )

    comment = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "row": "3"})
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        )
    )
    """
    COUNTRIES = [
        ("CL", "Chile"),
        ("VE", "Venezuela"),
        ("AR", "Argentina"),
        ("BR", "Brasil"),
    ]
    CONSOLES = [
        ("PC", "Master Race"),
        ("PS", "Play Station"),
        ("XB", "X-Box"),
        ("ND", "Nintendoodoo"),
    ]
    # Agregar los campos del formulario
    name = forms.CharField(label="Nombre", max_length=400)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=1)
    country = forms.MultipleChoiceField(choices=COUNTRIES)
    console = forms.ChoiceField(choices=CONSOLES)
    """
