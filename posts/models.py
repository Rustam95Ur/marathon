from django.db import models
from marathon.settings import POST_IMAGE_DIRECTORY


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to=POST_IMAGE_DIRECTORY, default='img/default_product_img.png',
                              verbose_name='Изображение', null=True)
    created_at = models.DateField()
    description = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return 'id: %d, Название блога: %s' % (
            self.id, self.title)
