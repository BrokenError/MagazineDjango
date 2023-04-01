from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import logout
from django.views.generic.edit import FormView, CreateView
from .forms import *
from django.urls import reverse_lazy


context = {
    'user': '',
    'title_links_user': [{'link': 'user', 'name':'Главная'},
                        {'link':'personal', 'name':'Личные данные'},
                        {'link':'security', 'name':'Безопасность и вход'}],
}

def user_info(request):
    context['user'] = User.objects.get(pk=request.user.id)
    return render(request, 'user/user-info.html', context=context)


def user_personal(request):
    return render(request, 'user/user-personal.html', context=context)


def user_security(request):
    return render(request, 'user/user-security.html', context=context)


def registration(request):
    return render(request, 'user/registration.html')

def logout_user(request):
    logout(request)
    return redirect('magazine_home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('magazine_home')