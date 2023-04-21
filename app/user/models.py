from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    bio = models.TextField('О себе', null=True, max_length=1000, blank=True)
    birth_date = models.DateField('День рождение', null=True, blank=True)
    profile_img = models.ImageField('Фото профиля', null=True, blank=True, upload_to="users/profile/")
    country = models.TextField('Страна', max_length=100 ,null=True, blank=True)
    city = models.TextField('Город', max_length=168 ,null=True, blank=True)
    phoneNumber = PhoneNumberField('Номер телефона', unique = True, null = True, blank = True)
    is_phone_verified = models.BooleanField(default=False)
    balance = models.DecimalField('Баланс', max_digits=8, decimal_places=2, blank=True, default=0)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        Profile.objects.create(username=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()