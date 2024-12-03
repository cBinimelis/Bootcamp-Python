from django.db import models

HEIGHT = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('B', 'Big'),
)

class Smartphone(models.Model):
    model = models.CharField(max_length=50)
    storage = models.CharField(max_length=50,default='')
    ram = models.CharField(max_length=50,default='')
    screen_size = models.CharField(max_length=50,default='')
    height = models.CharField(
        max_length=1,
        choices=HEIGHT,
        default='S'
    )
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)


class Meta:
    permissions = [
        ("can_publish", "Can publish smartphones"),
        ("can_view_details", "Can view detailed smartphone information"),
    ]


def __str__(self):
    return f"{self.model}"
