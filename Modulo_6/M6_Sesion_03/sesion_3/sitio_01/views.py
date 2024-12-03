from django.shortcuts import render
import datetime
from .forms import ContactForm


def home(request):
    first_name = "Cristofer"
    last_name = "Binimelis"
    context = {"first_name": first_name, "last_name": last_name}
    return render(request, "home.html", context)


def contact(request):

    print(request.method)

    date = datetime.datetime.now
    mail = "john@doe.com"
    phone = "555 9998 8887"
    form = ContactForm()
    context = {"mail": mail, "phone": phone, "date": date, "form": form}
    return render(request, "contact.html", context)


def about(request):
    enterprise_name = "Empresas Humildes"
    description = "Somos los mejores!!"
    context = {"enterprise_name": enterprise_name, "description": description}
    return render(request, "about.html", context)


def testimonials(request):
    testimonials = [
        {"name": "Maria", "testimonial": "Excelente servicio!"},
        {"name": "Juan", "testimonial": "No me gustó su música, devuélvase a Japón"},
    ]
    return render(request, "testimonials.html", context={"data": testimonials})
