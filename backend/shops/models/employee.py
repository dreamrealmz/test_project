from django.db import models
from django.core.validators import RegexValidator


class Employee(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?7?\d{7,11}$',
        message="Phone number must be entered in the format: '+799999999'. Up to 15 digits allowed."
    )
    name = models.CharField(verbose_name='Имя', max_length=64, default='')
    phone_number = models.CharField(verbose_name='Телефон', max_length=11, validators=[phone_regex], default='')

    def __str__(self):
        return f'{self.name} | {self.phone_number}'

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
