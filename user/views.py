from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


# Create your views here.

def mah_user_login(request):
    if request.user.profile.user_role == 'MAH_Employee':
        return render(request, 'home.html')

    elif request.user.profile.user_role == 'Local_Building_Manager':
        return render(request, 'home.html')

    else:
        return render(request, 'home.html')


def home(request):
    return render(request, 'mercyhousing/base.html',
                  {'mercyhousing': home})


def signup(request):
    if request.method == 'POST':
        user_form = CreateUserAccountForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")
    else:
        user_form = CreateUserAccountForm()
    return render(request, 'registration/signup.html', {'user_form': user_form})


@login_required
def profile_update(request):
    if request.method == 'POST':
        profile_form = CreateProfileAccountForm()
        usern = User.objects.filter(id=request.user.id)
        print(usern)
        for user in usern:
            role = request.POST.get('user_role')
            user.profile.user_role = role
            num = request.POST.get('user_contact_num')
            user.profile.user_contact_num = num
            skills = request.POST.get('user_skills')
            user.profile.user_skills = skills
            address1 = request.POST.get('user_address_1')
            user.profile.user_address_1 = address1
            address2 = request.POST.get('user_address_2')
            user.profile.user_address_2 = address2
            city = request.POST.get('user_city')
            user.profile.user_city = city
            state = request.POST.get('user_state')
            user.profile.user_state = state
            user.profile.user_profile_created_check = True
        return redirect("/")
    else:
        profile_form = CreateProfileAccountForm()
    return render(request, 'registration/profile_update.html', {'profile_form': profile_form})


def workorder_new(request):
    return render(request, 'workorder_new.html')
