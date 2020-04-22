from django.conf import settings
from django.db import models


class SearchQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                             verbose_name='Пользователь')
    query = models.CharField(u"Текст запроса", max_length=220, null=True, blank=True)
    timestamp = models.DateTimeField(u"Создан", auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

