"""Integrate with admin module."""

from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import *


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no mobile field."""
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'first_name', 'last_name', 'email')}),
        (
            _('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                          'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'date_joined')
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CarrierCategory)
class CarrierCategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'phone_number',
        'national_id',
        'user',
    ]
    search_fields = ['first_name', 'last_name', 'phone_number', 'national_id', 'user__id']


@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'phone_number',
        'national_id',
        'user',
        'category'
    ]
    search_fields = ['first_name', 'last_name', 'phone_number', 'national_id', 'user__id', 'category__title']


@admin.register(Organization)
class Admin(admin.ModelAdmin):
    list_display = [
        'name',
        'national_id',
        'user',
    ]
    search_fields = ['name', 'phone_number', 'user_id']


@admin.register(Employee)
class Admin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'phone_number',
        'national_id',
        'user',
        'company_id',
        'position'
    ]
    search_fields = ['first_name', 'last_name', 'phone_number', 'national_id', 'user__id', 'position', 'company_id']
