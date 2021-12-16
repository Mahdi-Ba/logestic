from django.contrib import admin

# Register your models here.
from apps.generals.models import *


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'country'
    ]
    search_fields = ['name']
    list_filter = ['country']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'state'
    ]
    search_fields = ['name']
    list_filter = ['state']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'country',
        'state',
        'city',
        'street',
        'house_number',
        'address',
        'phone',
        'user',
    ]
    search_fields = ['user__id', 'phone']
    list_filter = ['state']


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = [
        'number', 'color', 'user'
    ]
    search_fields = ['number', 'user__id']
