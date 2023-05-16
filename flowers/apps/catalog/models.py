from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Products(models.Model):
    title = models.CharField('Название', max_length=150, db_index=True)
    slug = models.SlugField('Слаг', max_length=150, unique=True)
    price = models.DecimalField('Стоимость', max_digits=10, decimal_places=2)
    description = models.TextField('Описание', max_length=1000, blank=True)
    photo = models.ImageField(upload_to="product/%Y/%m/%d", blank=True)
    available = models.BooleanField(default=True)
    date_created = models.DateTimeField('Дата появления товара', auto_now_add=True)
    date_uploaded = models.DateTimeField('Дата появления товара', auto_now=True)
    cat = models.ForeignKey('Categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-date_created']
        index_together = (('id', 'slug'),)


class Categories(models.Model):
    title = models.CharField('Название', max_length=50, db_index=True)
    slug = models.SlugField('Слаг', max_length=50, unique=True)
    date = models.DateTimeField('Дата появления')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-date']
