from django.shortcuts import render
from books.models import BookModel


def home(request):
    return render(request, "index.html")


def listbook(request):
    books = BookModel.objects.all()
    context = {"books": books}
    return render(request, "listbook.html", context)
