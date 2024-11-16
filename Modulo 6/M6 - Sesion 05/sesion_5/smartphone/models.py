from django.db import models


class Smartphone(models.Model):
    model = models.CharField(max_length=50)


class Meta:
    permissions = [
        ("can_publish", "Can publish smartphones"),
        ("can_view_details", "Can view detailed smartphone information"),
    ]


def __str__(self):
    return f"{self.model}"
