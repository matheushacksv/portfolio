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

@shared_task
def novo_contato(email, email_do_contato, name, objetivo, mensagem):
    assunto = f'Novo contato através do portfolio!'

    mensagem = f'''
Recebemos um novo contato através do portfólio!
Email: {email_do_contato}
Nome: {name}
Assunto: {objetivo}
Mensagem: {mensagem}
'''

    send_mail(
        assunto,
        mensagem,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )

