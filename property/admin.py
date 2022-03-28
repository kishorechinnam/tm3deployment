from django.contrib import admin
from .models import Property, Apartment


# Register your models here.
class PropertyList(admin.ModelAdmin):
    list_display = ('property_id', 'property_name', 'property_contact_num', 'property_apartment_id',)
    list_filter = ('property_id', 'property_name',)
    search_fields = ('property_id', 'property_name', 'property_contact_num', 'property_apartment_id',)
    ordering = ['property_id']


class ApartmentList(admin.ModelAdmin):
    list_display = ('apartment_id', 'apartment_name', 'apartment_contact_num', 'apartment_comments',
                    'apartment_num', 'apartment_building_num')
    list_filter = ('apartment_id', 'apartment_name', 'apartment_building_num')
    search_fields = ('apartment_id', 'apartment_name', 'apartment_contact_num',
                     'apartment_building_num',)
    ordering = ['apartment_id']


admin.site.register(Property, PropertyList)
admin.site.register(Apartment, ApartmentList)