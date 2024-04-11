from django.db.models.signals import post_init, post_save
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Client
from back.settings import DEFAULT_FROM_EMAIL


@receiver(post_save, sender=Client)
def notify_about_new_client(sender, instance, created, **kwargs):
    """ Сигнал фиксирующий создание нового клиента """
    #send_mail(
    #    subject='ExampleSubject',
    #    message='ExampleMessage',
    #    from_email=DEFAULT_FROM_EMAIL,
    #    recipient_list=['examplemail@mail.ru'],
    #)

    if created:
        # Создание содержимого письма на основе html шаблона
        context = {
            'name': instance.name,
            'surname': instance.fam,
            'create_time': instance.add_time.strftime('%d-%m-%Y %H:%M:%S'),
            'phone': instance.phone,
            'email': instance.email,
        }
        html_content1 = render_to_string(
            template_name='email_sending/email_content.html',
            context=context,
        )

        html_content2 = render_to_string(
            template_name='email_sending/email_to_client.html',
            context=context,
        )

        # Создание письма менеджеру
        manager_message = EmailMultiAlternatives(
            subject='First Class',
            body='',
            from_email=DEFAULT_FROM_EMAIL,
            to=[DEFAULT_FROM_EMAIL],
        )
        # Создание письма клиенту
        client_message = EmailMultiAlternatives(
            subject='First Class',
            body='',
            from_email=DEFAULT_FROM_EMAIL,
            to=[instance.email],
        )

        # Указание контента
        manager_message.attach_alternative(html_content1, 'text/html')
        client_message.attach_alternative(html_content2, 'text/html')

        # Отправка писем
        manager_message.send()
        client_message.send()
