from django.shortcuts import render
from django.views.generic import TemplateView


def platform(request):
    return render(request, 'platform.html')


class Games(TemplateView):
    template_name = 'games.html'


class Cart(TemplateView):
    template_name = 'cart.html'


