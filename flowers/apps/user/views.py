from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from apps.products.forms import LoginUserForm, RegisterUserForm
from .forms import SaveDataUser, SaveDataProfile, AddPhone

context = {
    'user': '',
    'title_links_user': [{'link': 'user', 'name': 'Главная'},
                         {'link': 'personal', 'name': 'Личные данные'},
                         {'link': 'security', 'name': 'Безопасность и вход'}],
    'cat_selected': '',
}


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'user/register.html'
    success_url = ""

    def form_valid(self, form):
        form.save()
        return super(RegisterUser, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterUser, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('magazine_home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'products/main.html'

    def form_valid(self, form):
        username = self.request.POST["username"]
        password = self.request.POST["password"]
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class ChangePassword(PasswordChangeView):
    form_class = SetPasswordForm
    template_name = 'user/user-info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_links_user'] = [{'link': 'user', 'name': 'Главная'},
                                       {'link': 'personal', 'name': 'Личные данные'},
                                       {'link': 'security', 'name': 'Безопасность и вход'}]
        context['title'] = 'Изменение пароля на сайте'
        context['user'] = User.objects.get(pk=self.request.user.id)
        context['cat_selected'] = 'Главная'
        return context

    def get_success_url(self):
        return reverse_lazy('user')


def user_info(request):
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
