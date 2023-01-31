# Django modules
from django.contrib import admin

# Project modules
from .models import Key, Keyboard


admin.site.register(Key)
admin.site.register(Keyboard)
