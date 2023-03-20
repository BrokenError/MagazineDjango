from django.db import models

class Profile(models.Model):
    username = models.TextField('Имя', max_length=50)
    bio = models.TextField('О себе', null=True, blank=True)
    profile_img = models.ImageField('Фото профиля', null=True, blank=True, upload_to="users/profile/")
    balance = models.DecimalField('Баланс', max_digits=8, decimal_places=2)