from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    discount_notifications = models.BooleanField(default=False)

    def __str__(self):
        return f'Profile for {self.user.username}'


class Item(models.Model):
    slug = models.SlugField('Унікальна назва', unique=True)
    title = models.CharField('Назва товару', max_length=200)
    image = models.ImageField('Основне фото', upload_to='items/', blank=True, null=True)
    desc = models.TextField('Опис товару')
    price = models.DecimalField('Ціна', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField('Додаткове фото', upload_to='items/')
    is_main = models.BooleanField('Основне зображення', default=False)

    def __str__(self):
        return f"{self.item.title} - {'Головне' if self.is_main else 'Інше'}"



class Order(models.Model):
    DELIVERY_CHOICES = [
        ('courier', 'Кур’єрська доставка'),
        ('pickup', 'Самовивіз'),
        ('post', 'Пошта')
    ]

    name = models.CharField('Імʼя', max_length=200)
    surname = models.CharField('Прізвище', max_length=200)
    email = models.CharField('Email', max_length=200)
    phone = models.CharField('Телефон', max_length=200)
    delivery_method = models.CharField('Спосіб доставки', max_length=20, choices=DELIVERY_CHOICES, default='courier')
    address = models.CharField('Адреса доставки', max_length=255)
    basket = models.JSONField('Кошик', default=list)

    def __str__(self):
        return f"{self.name} {self.surname} ({self.phone})"
