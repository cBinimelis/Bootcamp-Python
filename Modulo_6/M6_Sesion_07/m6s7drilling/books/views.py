from django.shortcuts import render
from .forms import BookForm


# Create your views here.
def inputbook(request):
    form = BookForm()
    context = {"form": form}
    return render(request, "inputbook.html", context)
