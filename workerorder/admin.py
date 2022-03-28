from django.contrib import admin
from .models import WorkOrder


# Register your models here.


class WorkOrderList(admin.ModelAdmin):
    list_display = ('short_desc', 'apartment_num', 'building_num', 'status', 'severity', 'assign_to',
                    'renter_name', 'manager_name', 'promised_date', 'completed_date', 'estimated_cost',
                    'actual_cost')
    list_filter = ('short_desc', 'status',)
    search_fields = ('short_desc', 'apartment_num', 'building_num', 'status')
    ordering = ['short_desc']


admin.site.register(WorkOrder, WorkOrderList)
