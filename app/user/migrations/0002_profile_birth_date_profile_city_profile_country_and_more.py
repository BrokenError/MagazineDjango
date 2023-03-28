# Generated by Django 4.1.7 on 2023-03-27 00:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='День рождение'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.TextField(blank=True, max_length=168, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, verbose_name='Баланс'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
