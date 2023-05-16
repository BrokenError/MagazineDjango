from django import forms
from apps.user.models import User
from .models import Profile


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
