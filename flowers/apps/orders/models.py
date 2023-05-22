from django.db import models
from apps.catalog.models import Products


class Order(models.Model):
    first_name = models.CharField('Фамилия', max_length=50)
    last_name = models.CharField('Имя', max_length=70)
    email = models.EmailField('Почта')
    created = models.DateTimeField('Дата создания', auto_now=True)
    paid = models.BooleanField('Оплачено', default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.заказ.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='Заказ', blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name='Товар', blank=True, on_delete=models.CASCADE)
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField('Количество', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
