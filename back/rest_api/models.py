from django.db import models

# Контактная информация клиента
class Client(models.Model):   
    name = models.CharField(max_length=50, verbose_name='Имя')
    fam = models.CharField(max_length=50, verbose_name='Фамилия')
    otc = models.CharField(max_length=50, null=True, blank=True, verbose_name='Отчество')
    email = models.EmailField()
    phone = models.TextField(max_length=50, verbose_name='Телефон')
