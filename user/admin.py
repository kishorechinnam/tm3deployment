from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
# class ProfileList(admin.ModelAdmin):
#     list_display = ('user', 'user_name', 'user_role', 'user_email', 'user_skills', 'user_address_1',
#                     'user_address_2', 'user_city', 'user_state')
#     list_filter = ('user', 'user_name',)
#     search_fields = ('user', 'user_name', 'user_email', 'user_address_1', 'user_address_2',
#                      'user_city', 'user_state')
#     ordering = ['user']
#
#
# admin.site.register(Profile, ProfileList)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
