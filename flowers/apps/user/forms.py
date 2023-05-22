from django import forms
from django.contrib.auth.forms import UserCreationForm

from apps.user.models import User, Profile


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


class AddPhone(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("phoneNumber",)


class VerifyForm(forms.Form):
    code = forms.CharField(max_length=8, required=True, help_text='Введите смс, отправленное на ваш телефон')

