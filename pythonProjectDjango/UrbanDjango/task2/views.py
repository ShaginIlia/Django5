from django.shortcuts import render
from django.views.generic import TemplateView


class ClassTp(TemplateView):
    template_name = 'class_template.html'


def func_tp(request):
    return render(request, 'func_template.html')



