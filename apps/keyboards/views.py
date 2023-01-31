# Django modules
from django.shortcuts import render
from django.views import View
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect
)

# Project modules
from .models import (
    Key,
    Keyboard
)
from .forms import (
    KeyForm,
    KeyboardForm
)


class KeyView(View):
    form = KeyForm

    def get(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        keys = Key.objects.all()

        return render(
            request=request,
            template_name='keyboards/keys.html',
            context={
                'ctx_keys': keys,
                'ctx_form': self.form(),
            }
        )

    def post(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        form: KeyForm = KeyForm(
            request.POST
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/key')

        return HttpResponse('Error!')

class KeyboardView(View):
    form = KeyboardForm

    def get(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        keyboards = Keyboard.objects.all()

        return render(
            request=request,
            template_name='keyboards/keyboards.html',
            context={
                'ctx_keyboards': keyboards,
                'ctx_form': self.form(),
            }
        )

    def post(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        form: KeyboardForm = KeyboardForm(
            request.POST
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/keyboard')

        return HttpResponse('Error!')
