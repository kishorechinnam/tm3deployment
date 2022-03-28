from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile
from django.contrib.auth.models import User


class CreateUserAccountForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, help_text='Required')
    last_name = forms.CharField(max_length=20, help_text='Required')
    email = forms.EmailField(max_length=60, help_text='Required')

    # address = forms.CharField(max_length=70, help_text='Required')
    # city = forms.CharField(max_length=50, help_text='Required')
    # zipcode = forms.CharField(max_length=10)
    # phone = forms.CharField(max_length=50)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')


class CreateProfileAccountForm(forms.ModelForm):
    USER_ROLE_CHOICES = [
        ('Local_Building_Manager', 'Local_Building_Manager'),
        ('Property_Manager', 'Property_Manager'),
        ('MAH_Employee', 'MAH_Employee'),
    ]
    user_role = forms.CharField(help_text='Required')
    user_contact_num = forms.IntegerField(help_text='Required')
    user_skills = forms.CharField(max_length=250, help_text='Required')
    # user_password = forms.CharField(max_length=100, help_text='Required')
    user_address_1 = forms.CharField(max_length=200, help_text='Required')
    user_address_2 = forms.CharField(max_length=200, help_text='Required')
    user_city = forms.CharField(max_length=100, help_text='Required')
    user_state = forms.CharField(max_length=100, help_text='Required')

    class Meta:
        model = Profile
        fields = ('user_role', 'user_contact_num', 'user_skills', 'user_password', 'user_address_1', 'user_address_2',
                  'user_city', 'user_state')
