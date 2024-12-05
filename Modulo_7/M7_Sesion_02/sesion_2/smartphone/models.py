from django.db import models

HEIGHT = (
    ("S", "Small"),
    ("M", "Medium"),
    ("B", "Big"),
)

STATUS = (
    ("disponible", "Disponible"),
    ("agotado", "Agotado"),
)


class Builder(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Smartphone(models.Model):
    builder = models.ForeignKey(
        Builder,
        on_delete=models.CASCADE,
        related_name="smartphone_builder",
        null="True",
    )
    model = models.CharField(max_length=50)
    storage = models.CharField(max_length=50, default="")
    ram = models.CharField(max_length=50, default="")
    screen_size = models.CharField(max_length=50, default="")
    height = models.CharField(max_length=1, choices=HEIGHT, default="S")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS, default="disponible")

    def __str__(self):
        return f"{self.model} - {self.storage} - {self.ram}"


class Meta:
    permissions = [
        ("can_publish", "Can publish smartphones"),
        ("can_view_details", "Can view detailed smartphone information"),
    ]


def __str__(self):
    return f"{self.model}"
