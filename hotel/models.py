from django.db import models
from django.contrib.auth import models as user_models


class CustomUser(user_models.AbstractUser):
    pass


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    stars = models.IntegerField()

    def __str__(self):
        return self.name


class Passport(models.Model):
    number = models.IntegerField()
    number_ser = models.IntegerField()
    date_of_birth = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.number}, {self.number_ser}"


class Visitor(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    passport = models.OneToOneField(Passport, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
