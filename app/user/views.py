from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic.edit import FormView

def user_login(request):
    return render(request, 'products/main.html')


def user_info(request):
    return render(request, 'products/main.html')


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = ""

    template_name = 'register.hmtl'

    # class Meta:
    #     model = User
    #     fields = ('username', 'password1', 'password2', 'photo')


    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)