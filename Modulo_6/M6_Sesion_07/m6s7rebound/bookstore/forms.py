from django import forms


class BookForm(forms.Form):
    title = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    author = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    score = forms.IntegerField(
        min_value=0,
        max_value=10000,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
