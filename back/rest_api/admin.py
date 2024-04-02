from django.contrib import admin
from .models import Client

# Регистрирую модели в админке
admin.site.register(Client)
