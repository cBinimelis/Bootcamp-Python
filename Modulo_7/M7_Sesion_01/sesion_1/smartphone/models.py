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


class Smartphone(models.Model):
    model = models.CharField(max_length=50)
    storage = models.CharField(max_length=50, default="")
    ram = models.CharField(max_length=50, default="")
    screen_size = models.CharField(max_length=50, default="")
    height = models.CharField(max_length=1, choices=HEIGHT, default="S")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS, default="disponible")

    def __str__(self):
        return f"{self.model} - {self.storage} - {self.ram}"


# class Maker (models.Model):
#    name=models.CharField(max_length=50, default='Samsung')
#    country = models.CharField(max_length=50,default='Korea')
#    smartphone =models.ForeignKey(Smartphone, on_delete=models.CASCADE,related_name='makers')


# -----------------------------------------------------
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="chapters")
    title = models.CharField(max_length=100)
    pages = models.PositiveIntegerField()

    def __str__(self):
        return f"Capitulo {self.title}: Pages:{self.pages}"


class Meta:
    permissions = [
        ("can_publish", "Can publish smartphones"),
        ("can_view_details", "Can view detailed smartphone information"),
    ]


def __str__(self):
    return f"{self.model}"
