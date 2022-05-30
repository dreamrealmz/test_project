from django.db import models


class Meet(models.Model):
    date_of_meeting = models.DateTimeField(verbose_name='Время посещения', auto_now_add=True)
    store = models.ForeignKey(verbose_name='Торговая точка',
                              on_delete=models.SET_NULL, null=True, blank=True, to='Store')
    latitude = models.FloatField(verbose_name='Долгота', default=0.0)
    longitude = models.FloatField(verbose_name='Широта', default=0.0)

    def __str__(self):
        return f'{self.store} | {self.date_of_meeting}'

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'
