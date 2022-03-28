from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    USER_ROLE_CHOICES = [
        ('Local_Building_Manager', 'Local_Building_Manager'),
        ('Property_Manager', 'Property_Manager'),
        ('Repair_Crew', 'Repair_Crew'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_name = models.CharField(max_length=200, blank=True)
    user_role = models.CharField(max_length=100, choices=USER_ROLE_CHOICES, blank=False, null=True)
    user_email = models.CharField(max_length=50, blank=True)
    user_email_1 = models.CharField(max_length=50, blank=True)
    user_contact_num = models.IntegerField(default=000, blank=True)
    user_skills = models.CharField(max_length=250, blank=True)
    user_password = models.CharField(max_length=100, blank=True)
    user_address_1 = models.CharField(max_length=200, blank=True)
    user_address_2 = models.CharField(max_length=200, blank=True)
    user_city = models.CharField(max_length=100, blank=True)
    user_state = models.CharField(max_length=100, blank=True)
    user_profile_created_check = models.BooleanField(default=False)

    # def __str__(self):
    #     return str(self.user)
    #
    # def profile(self):
    #     return str(self.user)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
