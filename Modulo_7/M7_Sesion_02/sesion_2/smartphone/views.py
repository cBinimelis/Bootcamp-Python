from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
from .models import Builder, Smartphone


@permission_required("smartphone.view_smartphone", raise_exception=True)
def home(request):
    return render(request, "smartphone/home.html")


@login_required
def create(request):
    builder = Builder.objects.create(name="Fabricante 1")

    phone = Smartphone.objects.create(
        model="smartphone 1",
        storage="128gb",
        ram=4,
        screen_size=6.98,
        height="M",
        price=16.5,
        status="disponible",
        builder=builder,
    )

    print(builder)
    print(phone)
    return render(request, "smartphone/home.html")


@login_required
def create_multiple(request):
    factories = [
        Builder(name="Fabricante 2"),
        Builder(name="Fabricante 3"),
    ]
    Builder.objects.bulk_create(factories)

    phones = [
        Smartphone(
            model="smartphone 2",
            storage="128gb",
            ram=4,
            screen_size=6.98,
            height="M",
            price=16.5,
            status="disponible",
            builder=factories[0],
        ),
        Smartphone(
            model="smartphone 3",
            storage="128gb",
            ram=4,
            screen_size=6.98,
            height="M",
            price=16.5,
            status="disponible",
            builder=factories[1],
        ),
    ]
    Smartphone.objects.bulk_create(phones)
    return render(request, "smartphone/home.html")


@login_required
def update(request):
    phone = Smartphone.objects.get(id=2)
    phone.model = "Smartphone 77"
    phone.storage = "512gb"
    phone.status = "agotado"
    phone.save()
    return render(request, "smartphone/home.html")


@login_required
def update_multiple(request):
    Smartphone.objects.filter(status="agotado").update(price=10.0)
    return render(request, "smartphone/home.html")
