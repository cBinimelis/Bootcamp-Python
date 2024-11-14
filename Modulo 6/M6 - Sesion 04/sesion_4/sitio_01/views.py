from django.shortcuts import render
import datetime
from .forms import ContactForm


def home(request):
    return render(request, "home.html")


def contact(request):

    print(request.method)
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")
