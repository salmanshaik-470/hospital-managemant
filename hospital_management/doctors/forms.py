from django.contrib.auth.models import User

from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


# class DoctorsForm(forms.ModelForm):
#     class Meta:
#         # model = DoctorsModel
#         fields = ['name', 'email', 'pwd', 'emp_id']
#         labels = {'name': 'Enter Name', 'email': 'Enter Email', 'pwd': 'Enter Password'}

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','first_name','last_name','email']