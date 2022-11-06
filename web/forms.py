from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import WebUser

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = WebUser
        fields = ("username","age","child","Marriage","work","work_address","hope_address","available_asset","password1", "password2", "email")

