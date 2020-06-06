from django.db import models


class Runner(models.Model):
    user_val = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'id: %d, Номер бегуна: %s' % (
            self.id, self.user_val)
