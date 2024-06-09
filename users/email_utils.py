import random
import logging
from django.core.mail import send_mail


logger = logging.getLogger(__name__)


def send_confirmation_email(user):
    """Отправка письма с подтверждением регистрации"""

    try:
        code = random.randint(100000, 999999)  # Генерация 6-значного кода
        user.confirmation_code = code  # Сохраняем код в модели пользователя
        user.save()
        subject = 'Код подтверждения регистрации'
        message = f'Ваш код подтверждения: {code}'
        from_email = 'andrey01590@gmail.com'
        send_mail(subject, message, from_email, [user.email])
        # email = EmailMessage(
        #     subject, message, to=[user.email],
        #     #  Вместо  from_email  используйте  'noreply@yourdomain.com'
        #     #  или  'noreply@example.com'  (если  у  вас  нет  своего  домена)
        #     from_email='andrey01590@gmail.com',
        # )
        # email.send()
    except Exception as e:
        logger.error(f"Ошибка при отправке письма: {e}")
