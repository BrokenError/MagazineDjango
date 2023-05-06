from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.views import LoginView
from .models import *
from .forms import *
from catalog.models import Products

class Login(LoginView):
    form_class = LoginUserForm
    second_form_class = RegisterUserForm
    template_name = 'products/main.html'

    
    def get_success_url(self):
        return reverse("magazine_home")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_images'] = Products.objects.all()[:8]
        if 'form' not in context:
            context['form'] = self.form_class(request=self.request)
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.get_form_class()
            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'

        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(**{form_name: form})


def user_basket(request):
    return render(request, 'products/basket.html')


