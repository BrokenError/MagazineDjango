from apps.products.forms import LoginUserForm, RegisterUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

from .forms import *


class SignupLoginView(FormView):
    template_name = 'products/main.html'
    success_url = "/"
    form_class = LoginUserForm
    second_form_class = RegisterUserForm

    def get_context_data(self, **kwargs):
        context = super(SignupLoginView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        return context

    def form_invalid(self, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        if 'form' in request.POST:
            form_class = self.get_form_class()
            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'
        # TODO nested IF
        form = self.get_form(form_class)
        if form.is_valid() and 'password2' not in form.data:
            user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
            if user is not None:
                login(request, user)
            else:
                form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(**{form_name: form})


context = {
    'user': '',
    'title_links_user': [{'link': 'user', 'name': 'Главная'},
                         {'link': 'personal', 'name': 'Личные данные'},
                         {'link': 'security', 'name': 'Безопасность и вход'}],
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
    context['verify'] = AddPhone()
    return render(request, 'user/user-security.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('magazine_home')


def verify_code(request):
    if request.method == 'POST':
        form = AddPhone(request.POST, instance=request.user.profile)
        if form.is_valid():
            request.user.profile.is_phone_verified = True
            request.user.save()
            return render(request, 'user/user-security.html', context=context)
    return redirect('magazine_home')


def delete_account(request):
    try:
        u = User.objects.get(pk=request.user.id)
        u.delete()
        return messages.success(request, "Аккаунт успешно удален")
    except User.DoesNotExist:
        return messages.error(request, "Пользователь не найден")
    except Exception:
        raise Http404
