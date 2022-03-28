from django.db import models


# Create your models here.
class Apartment(models.Model):
    apartment_id = models.IntegerField(primary_key=True)
    apartment_name = models.CharField(max_length=200, blank=True)
    apartment_contact_num = models.IntegerField()
    apartment_comments = models.CharField(max_length=200, blank=True)
    apartment_num = models.IntegerField()
    apartment_building_num = models.IntegerField()

    def __str__(self):
        return str(self.apartment_id)


class Property(models.Model):
    property_id = models.IntegerField(primary_key=True)
    property_name = models.CharField(max_length=200, blank=True)
    property_contact_num = models.IntegerField()
    property_apartment_id = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='property_apartment_id')

    # def completed(self):
    #     self.completed_date = timezone.now()
    #     self.save()

    def __str__(self):
        return str(self.property_id)