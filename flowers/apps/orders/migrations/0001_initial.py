# Generated by Django 3.2.19 on 2023-05-19 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='заказ', to='orders.order')),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='товар', to='catalog.products')),
            ],
        ),
    ]
