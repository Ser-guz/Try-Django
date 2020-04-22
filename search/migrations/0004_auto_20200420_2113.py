# Generated by Django 2.2 on 2020-04-20 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20200419_1611'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='searchquery',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Запрос', 'verbose_name_plural': 'Запросы'},
        ),
        migrations.AlterField(
            model_name='searchquery',
            name='query',
            field=models.CharField(blank=True, max_length=220, null=True, verbose_name='Текст запроса'),
        ),
        migrations.AlterField(
            model_name='searchquery',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='searchquery',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]