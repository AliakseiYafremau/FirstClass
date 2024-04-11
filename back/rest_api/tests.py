from django.test import TestCase
from django.core import mail
from django.contrib.auth.models import User
from rest_api.models import Client
from django.db.models.signals import post_save
from django.dispatch import receiver

from back.settings import DEFAULT_FROM_EMAIL


class ClientSignalTest(TestCase):
    def test_notify_about_new_client(self):
        # Убедимся, что начальное количество писем равно 0
        self.assertEqual(len(mail.outbox), 0)

        # Создаем нового клиента
        client = Client.objects.create(name='Ivan',
                                       fam='Ivanov',
                                       email='example@mail.ru',
                                       phone='123456789',)


        # Проверяем, что после создания клиента было отправлено два письма
        self.assertEqual(len(mail.outbox), 2)
        self.assertEqual(mail.outbox[0].to[0], DEFAULT_FROM_EMAIL)
        self.assertEqual(mail.outbox[1].to[0], client.email)

    def tearDown(self):
        mail.outbox.clear()

