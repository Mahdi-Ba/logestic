from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from apps.general.models import Address


class UserManager(BaseUserManager):
    """Define a model manager for User"""

    use_in_migrations = True

    def _create_user(self, username, password, extra_fields):
        """Create and save a User with the given username and password."""
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, extra_fields):
        extra_fields.pop('username')
        extra_fields.pop('password')
        """Create and save a regular User with the given username and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        """Create and save a SuperUser with the given mobile and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, password, **extra_fields)


class User(AbstractUser):
    """User model."""
    objects = UserManager()


class Status(models.Model):
    title = models.CharField(unique=True, null=False, max_length=250)

    def __str__(self):
        return self.title


class CarrierCategory(models.Model):
    title = models.CharField(unique=True, null=False, max_length=250)

    def __str__(self):
        return self.title


class Client(models.Model):
    first_name = models.CharField(unique=True, null=False, max_length=250)
    last_name = models.CharField(unique=True, null=False, max_length=250)
    phone_number = models.CharField(unique=True, null=False, max_length=250)
    national_id = models.CharField(unique=True, null=False, max_length=250)
    birthday = models.CharField(unique=True, null=False, max_length=250)
    address_alias = models.CharField(unique=True, null=False, max_length=250)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Carrier(models.Model):
    first_name = models.CharField(unique=True, null=False, max_length=250)
    last_name = models.CharField(unique=True, null=False, max_length=250)
    phone_number = models.CharField(unique=True, null=False, max_length=250)
    national_id = models.CharField(unique=True, null=False, max_length=250)
    birthday = models.CharField(unique=True, null=False, max_length=250)
    address_alias = models.CharField(unique=True, null=False, max_length=250)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(CarrierCategory, null=True, on_delete=models.SET_NULL)
    vehicle_id = models.CharField(unique=True, null=False, max_length=250)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Organization(models.Model):
    name = models.CharField(unique=True, null=False, max_length=250)
    phone_number = models.CharField(unique=True, null=False, max_length=250)
    national_id = models.CharField(unique=True, null=False, max_length=250)
    address_alias = models.CharField(unique=True, null=False, max_length=250)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Employee(models.Model):
    first_name = models.CharField(unique=True, null=False, max_length=250)
    last_name = models.CharField(unique=True, null=False, max_length=250)
    phone_number = models.CharField(unique=True, null=False, max_length=250)
    national_id = models.CharField(unique=True, null=False, max_length=250)
    company_id = models.CharField(unique=True, null=False, max_length=250)
    position = models.CharField(unique=True, null=False, max_length=250)
    birthday = models.CharField(unique=True, null=False, max_length=250)
    address_alias = models.CharField(unique=True, null=False, max_length=250)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
