# Django modules
from django.contrib.auth.models import AbstractUser

# Project modules
from abstracts.models import AbstractModel


class CustomUser(AbstractUser, AbstractModel):
    pass
