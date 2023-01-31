from django.db import models


class AbstractModel(models.Model):
    create_date = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )

    change_date = models.DateTimeField(
        verbose_name='дата изменения',
        auto_now=True
    )
