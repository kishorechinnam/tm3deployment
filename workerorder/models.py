from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class WorkOrder(models.Model):
    worker_id = models.IntegerField(primary_key=True)
    short_desc = models.CharField(max_length=300, blank=True)
    skill_set = models.CharField(max_length=200, blank=True)
    apartment_num = models.IntegerField()
    building_num = models.IntegerField()
    status = models.CharField(max_length=200)
    severity = models.CharField(max_length=200)
    assign_to = models.CharField(max_length=200)
    renter_name = models.CharField(max_length=200)
    manager_name = models.CharField(max_length=200)
    promised_date = models.DateTimeField()
    completed_date = models.DateTimeField(default=timezone.now)
    actual_cost = models.FloatField()
    estimated_cost = models.FloatField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    # property_id = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property')

    def created(self):
        self.promised_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.short_desc)
