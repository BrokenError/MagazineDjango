from django.contrib import admin
from .models import *


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    list_display_links = ('id', 'title')


class ProductsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Products)
