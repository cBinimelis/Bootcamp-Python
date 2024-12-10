from django.db import models


class Person(models.Model):
    fullname = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    createAt = models.DateTimeField(auto_now_add=True)
    salary_month = models.FloatField(default=0.0)
    salary_year = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    isActive = models.BooleanField(default=True)
    birthDate = models.DateField(null=True)
    dinnerTime = models.TimeField(null=True)
    facebookUrl = models.URLField(null=True)
    tag = models.SlugField(null=True)
    avatar = models.ImageField(null=True)
    curriculum = models.FileField(null=True)

    def __str__(self):
        return self.fullname


class Category(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Student(models.Model):
    fullname = models.CharField(max_length=100)


class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    biography = models.TextField()


class Estudiante(models.Model):
    fullname = models.CharField(max_length=100)
    courses = models.ManyToManyField("Course")


class Course(models.Model):
    name = models.CharField(max_length=50)


class Author(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField()


class Book(models.Model):
    title = models.CharField(max_length=50)
    publishAt = models.DateTimeField()

    authors = models.ManyToManyField("Author", through="Collaboration")


class Collaboration(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    role = models.CharField(max_length=10)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
