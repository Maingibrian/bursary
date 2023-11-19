from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import  User

class chequeform(ModelForm):
    class Meta:
        model =  institution
        fields = "__all__"

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',]

class universityform(ModelForm):
    class Meta:
        model = university
        fields = ['Name']