from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    slug = models.CharField(max_length=50)

    def __str__(self):
        return 'id: %d, Название: %s, Ссылка: %s' % (
            self.id, self.title, self.slug)
