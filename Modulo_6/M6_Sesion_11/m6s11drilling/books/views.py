from django.shortcuts import render
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .forms import BookForm, RegisterForm
from .models import BookModel


# Create your views here.
def inputbook(request):
    form = BookForm()
    context = {"form": form}
    return render(request, "inputbook.html", context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            content_type = ContentType.objects.get_for_model(BookModel)

            development = Permission.objects.get(
                codename="development", content_type=content_type
            )

            add_books = Permission.objects.get(
                codename="add_bookmodel", content_type=content_type
            )

            view_books = Permission.objects.get(
                codename="view_bookmodel", content_type=content_type
            )
            user = form.save()

            user.user_permissions.add(development, add_books, view_books)
            return render(request, "index.html")

    register_form = RegisterForm()
    context = {"register_form": register_form}
    return render(request, "register.html", context)
