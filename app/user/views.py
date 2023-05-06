from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import logout
from django.views.generic.edit import FormView, CreateView
from .forms import *
from . import verify
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib import messages

context = {
    'user': '',
    'title_links_user': [{'link': 'user', 'name':'Главная'},
                        {'link':'personal', 'name':'Личные данные'},
                        {'link':'security', 'name':'Безопасность и вход'}],
    'cat_selected': '',
}

def user_info(request):
    context['user'] = User.objects.get(pk=request.user.id)
    context['cat_selected'] = 'Главная'
    return render(request, 'user/user-info.html', context=context)


def user_personal(request):
    context['user'] = User.objects.get(pk=request.user.id)
    context['form'] = SaveDataUser()
    context['form2'] = SaveDataProfile()
    context['cat_selected'] = 'Личные данные'
    if request.method == 'POST':
        form = SaveDataUser(request.POST, instance=request.user)
        form2 = SaveDataProfile(request.POST, instance=request.user.profile)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            render(request, 'user/user-info.html', context=context)
        else:
            print('error')
    return render(request, 'user/user-personal.html', context=context)


def user_security(request):
    context['cat_selected'] = 'Безопасность и вход'
    return render(request, 'user/user-security.html', context=context)


def registration(request):
    return render(request, 'user/registration.html')

def logout_user(request):
    logout(request)
    return redirect('magazine_home')

# НУЖНА УЧЕТНАЯ ЗАПИСЬ TWILIO

# def verify_code(request):
#     if request.method == 'POST':
#         form2 = AddPhone(request.POST, instance=request.user.profile)
#         form = VerifyForm(request.POST)
#         context['verify'] = form
#         context['phone'] = form2

#         if form2.is_valid():
#             request.user.profile.save()
#             phone = request.user.profile.phoneNumber
#             verify.send(phone)

#         if form.is_valid():
#             code = form.cleaned_data.get('code')
#             if True:
#                 request.user.is_phone_verified = True
#                 request.user.save()
#                 return redirect('magazine_home')
#     else:
#         form = VerifyForm()
#     return render(request, 'user/verify.html', context=context)

def verify_code(request):
    if request.method == 'POST':
        form = AddPhone(request.POST, instance=request.user.profile)
        if form.is_valid():
            request.user.is_phone_verified = True
            request.user.save()
            return redirect('magazine_home')

    return render(request, 'user/verify.html', context=context)
    # return redirect('user')


def delete_account(request):
    try:
        u = User.objects.get(pk = request.user.id)
        u.delete()
        messages.success(request, "Аккаунт успешно удален")
    except User.DoesNotExist:
        messages.error("Пользователь не найден")
    except Exception as e:
        raise Http404
    return redirect('magazine_home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('magazine_home')