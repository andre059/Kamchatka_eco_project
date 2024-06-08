from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def generate_token(user):
    """Генерация токена для подтверждения регистрации"""
    return PasswordResetTokenGenerator().make_token(user)


def check_token(user, token):
    """Проверка токена для подтверждения регистрации"""

    return PasswordResetTokenGenerator().check_token(user, token)


def generate_confirmation_link(user):
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = generate_token(user)
    link = f'http://localhost:8000/{uidb64}/{token}'  # Замените 'http://localhost:8000' на URL вашего сайта
    return link
