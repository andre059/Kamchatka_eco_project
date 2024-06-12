from django.db import models

from users.models import NULLABLE, User


class Park(models.Model):
    """Парк"""

    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='parks/', **NULLABLE, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="обновлено")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Парк"
        verbose_name_plural = "Парки"


class Trail(models.Model):
    """Тропа"""

    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='trails/', **NULLABLE, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="обновлено")

    park = models.ForeignKey(Park, on_delete=models.CASCADE, verbose_name="Парк")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тропа"
        verbose_name_plural = "Тропы"


class Rule(models.Model):
    """Правило тропы"""

    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)
    rule_text = models.TextField(verbose_name="Правило")


class Notification(models.Model):
    """Уведомления"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE, verbose_name='тропа')
    type = models.CharField(max_length=255, choices=[('violation', 'Violation'), ('garbage', 'Garbage'),
                                                     ('event', 'Event')], verbose_name='тип')
    message = models.TextField(verbose_name="Сообщение")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")