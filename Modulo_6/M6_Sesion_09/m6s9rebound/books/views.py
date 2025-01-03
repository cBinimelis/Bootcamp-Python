from django.shortcuts import render
from .forms import BookForm, RegisterForm


# Create your views here.
def inputbook(request):
    form = BookForm()
    context = {"form": form}
    return render(request, "inputbook.html", context)


def register(request):
    register_form = RegisterForm()
    context = {"register_form": register_form}
    return render(request, "register.html", context)
