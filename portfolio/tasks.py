from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def enviar_email_contato(email):
    assunto = f'Recebi sua mensagem!'

    mensagem = '''Olá! 

Recebi sua mensagem e entrarei em contato o mais breve possível.

Atenciosamente,
'''

    send_mail(
        assunto,
        mensagem,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )

