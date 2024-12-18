from django.shortcuts import render, redirect
from .models import Order, OwnerEquipment, User
from equipments.models import Equipment


# Create your views here.
def order_list(request):
    orders = Order.objects.all()
    context = {"orders": orders}
    return render(request, "order/order_list.html", context)


def check_create(request):
    if request.method == "POST":
        employees = User.objects.filter(is_staff=True)
        action = request.POST["action"]
        if action == "check":
            serial = request.POST.get("serial")
            rut = request.POST.get("rut")
            equipment = Equipment.objects.filter(serial=serial).first()
            if equipment:
                owner_equipment = OwnerEquipment.objects.filter(
                    equipment=equipment, is_active=True
                ).first()
                if owner_equipment.user.profile.rut == rut:
                    context = {
                        "action": "create_order",
                        "employees": employees,
                        "equipment": equipment,
                    }
                else:
                    context = {"action": "change_owner"}
            else:
                context = {"action": "create_all"}
        elif action == "create_order":
            equipment_id = request.POST.get("equipment_id")
            employee_id = request.POST.get("employee_id")
            description = request.POST.get("description")
            equipment = Equipment.objects.get(pk=equipment_id)
            employee = User.objects.get(pk=employee_id)
            order = Order(
                equipment=equipment, employee=employee, description=description
            )
            order.save()
            return redirect("orders:home")
    else:
        context = {"action": "check"}
    return render(request, "order/check_create.html", context)
