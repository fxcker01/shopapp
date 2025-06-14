# Generated by Django 5.0.4 on 2025-05-12 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='items/', verbose_name='Картинка')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основне зображення')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.item')),
            ],
        ),
    ]
