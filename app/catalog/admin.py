from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'date']
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'image_show', 'price', 'available', 'date_created', 'date_uploaded']
    list_filter = ['available', 'date_created', 'date_uploaded']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('title',)}


    def image_show(self, obj):
        if obj.photo:
            return mark_safe("<img src='{}' width='50' />".format(obj.photo.url))
        return 'None'

    image_show.__name__ = "Картинка"
