# Django modules
from django import forms

# Project moduels
from .models import Key, Keyboard


class KeyForm(forms.ModelForm):
    """ Key model form """
    class Meta:
        model = Key
        fields = '__all__'


class KeyboardForm(forms.ModelForm):
    """ Keyboard model form """
    class Meta:
        model = Keyboard
        fields = '__all__'
        widgets = {
            'keys': forms.CheckboxSelectMultiple
        }
