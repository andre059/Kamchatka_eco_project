from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


def send_confirmation_email(user):
    """Отправка письма с подтверждением регистрации"""

    subject = 'Confirm your registration'
    message = (f'Hi {user.username}, \n Please confirm your registration by clicking this link: \n '
               f'{generate_confirmation_link(user)}')
    from_email = 'your_email@gmail.com'
    send_mail(subject, message, from_email, [user.email])


def generate_token(user):
    """Генерация токена для подтверждения регистрации"""

    return PasswordResetTokenGenerator().make_token(user)


def generate_confirmation_link(user):
    """Генерация ссылки для подтверждения регистрации"""

    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = generate_token(user)
    link = f'http://localhost:8000/confirm/{uidb64}/{token}'
    return link
