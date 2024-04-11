from django.test import TestCase
from django.core import mail
from django.contrib.auth.models import User
from rest_api.models import Client
from django.db.models.signals import post_save
from django.dispatch import receiver


class ClientSignalTest(TestCase):
    def test_notify_about_new_client(self):
        # Убедимся, что начальное количество писем равно 0
        self.assertEqual(len(mail.outbox), 0)

        # Создаем нового клиента
        client = Client.objects.create(name='Ivan',
                                       fam='Ivanov',
                                       otc='Ivanovich',
                                       email='example@mail.ru',
                                       phone='123456789',
                                       number='5',
                                       continent='AS',
                                       type='FAM')

        # Проверяем, что после создания клиента было отправлено одно письмо
        self.assertEqual(len(mail.outbox), 1)

    def tearDown(self):
        mail.outbox.clear()

