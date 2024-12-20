from django.shortcuts import render, redirect
from .models import Order, OwnerEquipment, User, Profile
from equipments.models import Equipment


# Create your views here.
def order_list(request):
    orders = Order.objects.all()
    context = {"orders": orders}
    return render(request, "orders/order_list.html", context)


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
                    user = Profile.objects.filter(rut=rut).first()
                    if user:
                        context = {
                            "action": "change_owner",
                            "equipment": equipment,
                            "user": user,
                        }
                    else:
                        context = {
                            "action": "change_owner",
                            "equipment": equipment,
                            "user": None,
                        }
            else:
                owner = Profile.objects.filter(rut=rut).first()
                form = EquipmentForm()
                context = {"action": "create_equipment", "user": owner, "form": form}
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
        elif action == "change_owner":
            rut = request.POST.get("rut")
            equipment_id = request.POST.get("equipment_id")
            equipment = Equipment.objects.get(pk=equipment_id)
            owner_equipment = OwnerEquipment.objects.filter(
                equipment=equipment, is_active=True
            ).first()
            owner_equipment.is_active = False
            owner_equipment.save()
            if rut:
                first_name = request.POST.get("first_name")
                last_name = request.POST.get("last_name")
                new_user = User(
                    first_name=first_name,
                    last_name=last_name,
                    username=rut,
                    password=rut,
                )
                new_user.save()

                new_owner = OwnerEquipment(equipment=equipment, user=new_user)
                new_owner.save()
            else:
                user_id = request.POST.get("user_id")
                user = User.objects.get(pk=user_id)
                new_owner = OwnerEquipment(equipment=equipment, user=user)
                new_owner.save()

            context = {
                "action": "create_order",
                "employees": employees,
                "equipment": equipment,
            }
        elif action == "create_equipment":
            user_id = request.POST.get("user_id")
            owner = User.objects.get(pk=user_id)

            equipment_form = EquipmentForm(request.POST)
            equipment = equipment_form.save()

            owner_equipment = OwnerEquipment(equipment=equipment, user=owner)
            owner_equipment.save()

            context = {
                "action": "create_order",
                "employees": employees,
                "equipment": equipment,
            }

    else:
        context = {"action": "check"}

    return render(request, "orders/check_create.html", context=context)
