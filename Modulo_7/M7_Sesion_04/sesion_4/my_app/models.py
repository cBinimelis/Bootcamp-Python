from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    monthly_salary = models.FloatField(default=0.0, null=True)
    yearly_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    is_active = models.BooleanField(default=True, null=True)
    birthday = models.DateField(null=True)
    dinner_time = models.TimeField(null=True)
    facebook_page = models.URLField(null=True)
    tag = models.SlugField(null=True)
    avatar = models.ImageField(null=True)
    curriculum = models.FileField(null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class User(models.Model):
    name = models.CharField(max_length=500)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    cursos = models.ManyToManyField("Curso")


class Curso(models.Model):
    nombre = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateField()
    authors = models.ManyToManyField("Author", through="Collaboration")


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()


class Collaboration(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
