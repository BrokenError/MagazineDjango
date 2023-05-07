from django.shortcuts import render
from django.db.models import Q
from django.views.generic.edit import FormView
from django.urls import reverse
from .models import *
from .forms import *
from catalog.models import Products
from django.contrib.auth import authenticate, login


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

        form = self.get_form(form_class)
        print(form)
        if form.is_valid():
            if 'password2' not in form.data:
                user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
                if user is not None:
                    login(request, user)
            else:
                form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(**{form_name: form})


def user_basket(request):
    return render(request, 'products/basket.html')


