from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(unique=True, null=False, max_length=250)


class State(models.Model):
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    name = models.CharField(unique=True, null=False, max_length=250)


class City(models.Model):
    state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)
    name = models.CharField(unique=True, null=False, max_length=250)


class Address(models.Model):
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    street = models.CharField(null=False, max_length=32)
    house_number = models.CharField(null=False, max_length=32)
    address = models.CharField(null=False, max_length=32)
    phone = models.CharField(null=True, max_length=32)

    def __str__(self):
        return self.title
