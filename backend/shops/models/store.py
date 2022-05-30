from django.db import models


class Store(models.Model):
    name = models.CharField(verbose_name='Название', max_length=64, default='')
    employee = models.ForeignKey(verbose_name='Работник', on_delete=models.CASCADE, to='Employee')

    def __str__(self):
        return f'{self.name} | {self.employee.name}'

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'
