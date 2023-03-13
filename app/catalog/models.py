from django.db import models

class Products(models.Model):
    title = models.CharField('Название', max_length=50)
    cost = models.DecimalField('Стоимость', max_digits=10, decimal_places=2)
    full_text = models.TextField('Описание')
    photo = models.ImageField(blank=True)
    date = models.DateTimeField('Дата появления товара')
    cat = models.ForeignKey('Categories', on_delete=models.PROTECT)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return f'/products/{self.id}'


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-date']


class Categories(models.Model):
    title = models.CharField('Название', max_length=50)
    date = models.DateTimeField('Дата появления')


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return f'/categories/{self.id}'


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-date']
