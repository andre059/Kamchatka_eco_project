# Generated by Django 5.0.2 on 2024-06-09 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_confirmation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.IntegerField(blank=True, max_length=6, null=True, verbose_name='код подтверждения'),
        ),
    ]
