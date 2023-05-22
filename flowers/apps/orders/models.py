from django.contrib.auth.models import User
from django.db import models

from apps.catalog.models import Products


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField('Описание', blank=True, null=True, max_length=300)
    deliv_address = models.CharField('Адрес доставки', blank=False, max_length=150)
    created = models.DateTimeField('Дата создания', auto_now=True)
    paid = models.BooleanField('Оплачено', default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.Заказ.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='Заказ', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name='Товар', on_delete=models.CASCADE)
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField('Количество', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
