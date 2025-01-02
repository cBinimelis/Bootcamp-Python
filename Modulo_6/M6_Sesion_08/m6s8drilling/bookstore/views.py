from django.shortcuts import render
from books.models import Book


def home(request):
    return render(request, "index.html")


def listbook(request):
    books = [
        Book(
            "Django 3 Web Development Cookbook, Fourth Edition",
            "Aidas Bendoratis",
            3250,
        ),
        Book("Two Scoops of Django 3.X", "Daniel Feldroy", 1570),
        Book("El Libro de Django", "Adrian Holovaty", 1400),
        Book("Python Web Development with Django", "Jeff Forcier", 1490),
        Book("Django for Professionals", "William S. Vincent", 2100),
        Book("Django for APIs", "William S. Vincent", 2540),
    ]
    context = {"books": books}
    return render(request, "listbook.html", context)


def login_view(request):
    pass
