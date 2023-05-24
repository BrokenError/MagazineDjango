from django.contrib.auth.models import User
from django.db import models

from apps.catalog.models import Products


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField('Дата создания', auto_now=True, max_length=0)
    description = models.CharField('Описание', blank=True, null=True, max_length=300)
    deliv_address = models.CharField('Адрес доставки', blank=False, max_length=150)
    paid = models.BooleanField('Оплачено', default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.id, self.description, self.deliv_address, self.created, self.paid)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.linkorder.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='linkorder', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name='Товар', on_delete=models.CASCADE)
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField('Количество', default=1)

    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.product, self.price, self.quantity)

    def get_cost(self):
        return self.price * self.quantity
