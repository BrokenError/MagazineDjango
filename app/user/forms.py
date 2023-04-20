from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django import forms
from django.core.exceptions import ValidationError
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import Textarea, TextInput, DateTimeInput
# from captcha.fields import CaptchaField


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        

class SaveDataUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")


class SaveDataProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "country", "city", "birth_date")
