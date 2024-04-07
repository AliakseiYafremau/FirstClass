from django.db.models.signals import post_init
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import Client
from back.settings import DEFAULT_FROM_EMAIL


@receiver(post_init, sender=Client)
def notify_about_new_client(sender, instance, **kwargs):
    """ Сигнал фиксирующий создание нового клиента """
    send_mail(
        subject='ExampleSubject',
        message='ExampleMessage',
        from_email=DEFAULT_FROM_EMAIL,
        recipient_list=['examplemail@mail.ru'],
    )