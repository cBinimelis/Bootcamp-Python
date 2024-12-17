from django.shortcuts import render
from .models import Order


# Create your views here.
def order_list(request):
    orders = Order.objects.all()
    context = {"orders": orders}
    return render(request, "order/order_list.html", context)
