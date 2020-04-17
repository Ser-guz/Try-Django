from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(u"Слаг", unique=True)
    title = models.CharField(u"Заголовок", max_length=50)
    content = models.TextField(u"Текст публикации", null=True, blank=True, max_length=6050)

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_edit_url(self):
        return f"/blog/{self.slug}/edit"

    def get_delete_url(self):
        return f"/blog/{self.slug}/delete"