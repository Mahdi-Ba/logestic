from django.contrib import admin

# Register your models here.
from apps.cores.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title'
    ]


@admin.register(ParcelStatus)
class ParcelStatusAdmin(admin.ModelAdmin):
    list_display = [
        'title'
    ]


@admin.register(InvoiceStatus)
class InvoiceStatusAdmin(admin.ModelAdmin):
    list_display = [
        'title'
    ]


@admin.register(ParcelWarehouseStatus)
class ParcelWarehouseStatusAdmin(admin.ModelAdmin):
    list_display = [
        'title'
    ]


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'code', 'address_alias', 'manager'
    ]
    search_fields = ['title', 'code', 'manager__id', 'address__id']


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'user',
        'code',
        'delivery_code',
        'internal',
        'price',
        'tax',
        'status',
    ]
    search_fields = ['name', 'user__id']
    list_filter = ['status','internal']

@admin.register(Parcel)
class ParceleAdmin(admin.ModelAdmin):
    list_display = [
      'name',
      'weight',
      'height',
      'length',
      'width',
      'price',
      'address',
      'address_alias',
      'user',
      'invoice',
      'status',
    ]
    search_fields = ['name', 'user__id','invoice__id']
    list_filter = ['status']




@admin.register(ParcelHistory)
class ParceleAdmin(admin.ModelAdmin):
    list_display = [
        'parcel',
        'user',
        'start_time',
        'end_time',
        'active',
        'status',

    ]
    search_fields = ['user__id','parcel__id']
    list_filter = ['status','active','start_time','end_time']



@admin.register(ParcelWarehouse)
class ParcelWarehouseAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'parcel',
        'warehouse',
        'weight',
        'height',
        'length',
        'start_time',
        'end_time',
        'active',
        'status',

    ]
    search_fields = ['user__id','parcel__id','warehouse__title','warehouse__code']
    list_filter = ['status','active','start_time','end_time']

@admin.register(ParcelDelivery)
class ParcelDeliveryAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'parcel',
        'warehouse',
        'weight',
        'height',
        'length',
        'time'


    ]
    search_fields = ['user__id', 'parcel__id', 'warehouse__title', 'warehouse__code']

