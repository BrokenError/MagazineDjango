from django.db import models

class Categories(models.Model):
    title = models.CharField('Название', max_length=50)
    cost = models.DecimalField('Стоимость', max_digits=10, decimal_places=2)
    full_text = models.TextField('Описание')
    date = models.DateTimeField('Дата появления')


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return f'/catalog/{self.id}'


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'