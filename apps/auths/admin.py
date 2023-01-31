# Django modules
from django.contrib import admin

#  Project modules
from .models import CustomUser

admin.site.register(CustomUser)
