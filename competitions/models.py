from django.db import models
from marathon.settings import COMPETITION_IMAGE_DIRECTORY


class Competition(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to=COMPETITION_IMAGE_DIRECTORY, default='img/default_product_img.png',
                              verbose_name='Изображение', null=True)
    start_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'id: %d, Название: %s, Статус: %s' % (
            self.id, self.title, self.is_active)
