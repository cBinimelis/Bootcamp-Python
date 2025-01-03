from django.shortcuts import render
from books.models import BookModel


def home(request):
    return render(request, "index.html")


def listbook(request):
    books = [
        BookModel(
            "Django 3 Web Development Cookbook, Fourth Edition",
            "Aidas Bendoratis",
            3250,
        ),
        BookModel("Two Scoops of Django 3.X", "Daniel Feldroy", 1570),
        BookModel("El Libro de Django", "Adrian Holovaty", 1400),
        BookModel("Python Web Development with Django", "Jeff Forcier", 1490),
        BookModel("Django for Professionals", "William S. Vincent", 2100),
        BookModel("Django for APIs", "William S. Vincent", 2540),
    ]
    context = {"books": books}
    return render(request, "listbook.html", context)


def login_view(request):
    pass
