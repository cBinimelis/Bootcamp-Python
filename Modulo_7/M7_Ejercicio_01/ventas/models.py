from django.db import models


# Create your models here.
class ClientAddress(models.Model):
    commune = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number = models.IntegerField()


class Client(models.Model):
    RUT = models.CharField(max_length=12)
    name = models.CharField(max_length=50)
    phones = models.CharField(max_length=100)
    address = models.ForeignKey(ClientAddress, on_delete=models.CASCADE)


class ProviderAddress(models.Model):
    commune = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number = models.IntegerField()


class Provider(models.Model):
    RUT = models.CharField(max_length=12)
    name = models.CharField(max_length=50)
    web = models.URLField(max_length=100)
    address = models.ForeignKey(ProviderAddress, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)


class Sale(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    products = models.ManyToManyField("Product", through="Detail")
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class Detail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)

    quantity = models.IntegerField()
