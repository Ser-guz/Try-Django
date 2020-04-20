from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q


User = settings.AUTH_USER_MODEL


# пользовательский QuerySet (а не дефолтный), поэтому после return нет super().
# super() применяется только для дефотного QuerySet.
class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(slug__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(user__username__icontains=query)
        )
        return self.filter(lookup)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)

class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    slug = models.SlugField(u"Слаг", unique=True)
    title = models.CharField(u"Заголовок", max_length=50)
    content = models.TextField(u"Текст публикации", null=True, blank=True, max_length=6050)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # имя менеджера "objects" обычно идет по умолчанию, но при создании пользовательского QuerySet'a нужно
    # менеджер вызывать еще раз.
    objects = BlogPostManager()

    class Meta:
        ordering = ['-publish_date', '-timestamp', '-updated'] # сортировка

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_edit_url(self):
        return f"/blog/{self.slug}/edit"

    def get_delete_url(self):
        return f"/blog/{self.slug}/delete"