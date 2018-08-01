from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import WMHUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = WMHUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = WMHUser
        fields = ('username', 'email')
