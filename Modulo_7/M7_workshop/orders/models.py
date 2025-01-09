from django.db import models
from equipments.models import Equipment
from django.contrib.auth.models import User

STATUSES = [
    ("received", "Recibido"),
    ("doing", "Reparación"),
    ("tests", "Pruebas"),
    ("ready", "Listo"),
    ("delivered", "Entregado"),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=10)


class OwnerEquipment(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Order(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now=True)
    delivered_at = models.DateTimeField(null=True)
    status = models.CharField(max_length=15, choices=STATUSES, default="received")

    @property
    def owner_equipment(self):
        owner_filtered = OwnerEquipment.objects.filter(
            is_active=True, equipment=self.equipment
        ).first()

        return owner_filtered.user.profile

    @property
    def owner_rut(self):
        return self.owner_equipment.rut

    @property
    def owner_name(self):
        return self.owner_equipment.user.get_full_name()


class Detail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
