# Django modules
from django.urls import path

# Project modules
from .views import (
    KeyView,
    KeyboardView
)


urlpatterns = [
    path('key/', KeyView.as_view()),
    path('keyboard/', KeyboardView.as_view()),
]
