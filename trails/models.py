from django.db import models

from users.models import NULLABLE


class Trail(models.Model):
    """Тропа"""

    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='trails/', **NULLABLE, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="обновлено")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тропа"
        verbose_name_plural = "Тропы"
