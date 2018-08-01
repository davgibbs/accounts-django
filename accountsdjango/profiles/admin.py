from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import WMHUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = WMHUser
    list_display = ['email', 'username', 'nickname']
    fieldsets = [
           (None, {'fields': ['username', 'email', 'nickname', 'password']})
       ]

admin.site.register(WMHUser, CustomUserAdmin)
