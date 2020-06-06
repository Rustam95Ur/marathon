from django.db import models
from runners.models import Runner
from competitions.models import Competition
from marathon.settings import PHOTO_IMAGE_DIRECTORY


class Photo(models.Model):
    runner = models.ForeignKey(Runner, on_delete=models.CASCADE, verbose_name='Бегун')
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, verbose_name='Соревнование')
    image = models.ImageField(upload_to=PHOTO_IMAGE_DIRECTORY, default='img/default_product_img.png',
                              verbose_name='Изображение', null=True)
    price = models.IntegerField()

    def __str__(self):
        return 'id: %d, Номер бегуна: %s, Соревнование: %s, Цена %s' % (
            self.id, self.runner.user_val, self.competition.title, self.price)
