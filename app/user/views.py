from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import logout
from django.views.generic.edit import FormView, CreateView
from .forms import *
from django.urls import reverse_lazy

def user_info(request):
    username = User.objects.get(pk=request.user.id)
    return render(request, 'user/user-info.html', {'user': username})

def registration(request):
    return render(request, 'user/registration.html')

def logout_user(request):
    logout(request)
    return redirect('magazine_home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('magazine_home')