from django import forms
from .models import WorkOrder


class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = ('short_desc', 'skill_set', 'apartment_num', 'building_num', 'status', 'severity', 'assign_to', 'renter_name', 'manager_name', 'promised_date', 'completed_date', 'actual_cost', 'estimated_cost', 'user_id')