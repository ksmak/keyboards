# Django modules
from django.db import models

# Project moduels
from abstracts.models import AbstractModel


class Key(AbstractModel):
    """ Key model """
    symbol = models.CharField(
        verbose_name='символ клавиши',
        max_length=1,
        unique=True
    )

    def __str__(self) -> str:
        return f'Клавиша: {self.symbol}'

    class Meta:
        verbose_name = 'клавиша'
        verbose_name_plural = 'клавиши'
        ordering = ('symbol', )


class Keyboard(AbstractModel):
    """ Keyboard model """
    keys = models.ManyToManyField(
        verbose_name='клавиши',
        to=Key,
        related_name='keys'
    )

    def __str__(self) -> str:
        return f'Клавиатура: {self.pk}'

    class Meta:
        verbose_name = 'клавиатура'
        verbose_name_plural = 'клавиатуры'
