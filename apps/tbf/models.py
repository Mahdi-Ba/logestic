from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from apps.general.models import Country, State, City, Address


#
# class Address(models.Model):
#     country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
#     state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)
#     city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
#     street = models.CharField(null=False, max_length=32)
#     house_number = models.CharField(null=False, max_length=32)
#     address = models.CharField(null=False, max_length=32)
#     phone = models.CharField(null=True, max_length=32)
#
#     def __str__(self):
#         return self.title


class Category(models.Model):
    title = models.CharField(unique=True, null=False, max_length=250)

    def __str__(self):
        return self.title


class ParcelStatus(models.Model):
    title = models.CharField(unique=True, null=False, max_length=250)

    def __str__(self):
        return self.title


class InvoiceStatus(models.Model):
    title = models.CharField(unique=True, null=False, max_length=250)

    def __str__(self):
        return self.title


class ParcelHistoryStatus(models.Model):
    title = models.CharField(unique=True, null=False, max_length=250)

    def __str__(self):
        return self.title


class ParcelWarehouseStatus(models.Model):
    title = models.CharField(unique=True, null=False, max_length=250)

    def __str__(self):
        return self.title


class Warehouse(models.Model):
    title = models.CharField(unique=True, null=False, max_length=250)
    code = models.CharField(unique=True, null=False, max_length=250)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    address_alias = models.CharField(unique=True, null=False, max_length=250)
    manager = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Invoice(models.Model):
    name = models.CharField(unique=True, null=False, max_length=250)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    code = models.CharField(unique=True, null=False, max_length=250)
    delivery_code = models.CharField(unique=True, null=False, max_length=250)
    internal = models.BooleanField(null=False)
    price = models.CharField(unique=True, null=False, max_length=250)
    tax = models.CharField(unique=True, null=False, max_length=250)
    status = models.ForeignKey(InvoiceStatus, null=True, on_delete=models.SET_NULL)


class Parcel(models.Model):
    name = models.CharField(unique=True, null=False, max_length=250)
    weight = models.CharField(unique=True, null=False, max_length=250)
    height = models.CharField(unique=True, null=False, max_length=250)
    length = models.CharField(unique=True, null=False, max_length=250)
    width = models.CharField(unique=True, null=False, max_length=250)
    price = models.CharField(unique=True, null=False, max_length=250)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    address_alias = models.CharField(unique=True, null=False, max_length=250)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    invoice = models.ForeignKey(Invoice, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(ParcelStatus, null=True, on_delete=models.SET_NULL)


class ParcelHistory(models.Model):
    parcel = models.ForeignKey(Parcel, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    start_time = models.TimeField()
    end_time = models.TimeField()
    active = models.BooleanField()
    status = models.ForeignKey(ParcelHistoryStatus, null=True, on_delete=models.SET_NULL)
    image = models.CharField(null=False, max_length=250)


class ParcelWarehouse(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    parcel = models.ForeignKey(Parcel, null=True, on_delete=models.SET_NULL)
    warehouse = models.ForeignKey(Warehouse, null=True, on_delete=models.SET_NULL)
    weight = models.CharField(unique=True, null=False, max_length=250)
    height = models.CharField(unique=True, null=False, max_length=250)
    length = models.CharField(unique=True, null=False, max_length=250)
    start_time = models.TimeField()
    end_time = models.TimeField()
    active = models.BooleanField()
    status = models.ForeignKey(ParcelWarehouseStatus, null=True, on_delete=models.SET_NULL)
    image = models.CharField(null=False, max_length=250)


class ParcelDelivery(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    parcel = models.ForeignKey(Parcel, null=True, on_delete=models.SET_NULL)
    warehouse = models.ForeignKey(Warehouse, null=True, on_delete=models.SET_NULL)
    weight = models.CharField(unique=True, null=False, max_length=250)
    height = models.CharField(unique=True, null=False, max_length=250)
    length = models.CharField(unique=True, null=False, max_length=250)
    time = models.TimeField()
    image = models.CharField(null=False, max_length=250)
