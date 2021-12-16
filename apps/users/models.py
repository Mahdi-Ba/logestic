from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models



class UserManager(BaseUserManager):
    def _create_user(self, username, password=None, extra_fields=None):
        """
        Creates and saves a User with the given username, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, extra_fields=None):
        if extra_fields is not None:
            extra_fields = dict(extra_fields)
            if extra_fields != {}:
                extra_fields.pop('username', None)
                extra_fields.pop('password', None)
                extra_fields.setdefault('is_staff', False)
                extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, password, extra_fields)

    def create_superuser(self, username, password, email=None):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self._create_user(
            username=username,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    objects = UserManager()

    def __str__(self):
        return self.username


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
    category = models.ForeignKey(CarrierCategory, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Organization(models.Model):
    name = models.CharField(unique=True, null=False, max_length=250)
    phone_number = models.CharField(unique=True, null=False, max_length=250)
    national_id = models.CharField(unique=True, null=False, max_length=250)
    address_alias = models.CharField(unique=True, null=False, max_length=250)
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
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

