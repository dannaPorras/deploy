from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import prueba

# Create your views here.


class PruebaView(TemplateView):
    template_name = "prueba.html"


class PruebaListView(ListView):
    model = prueba
    template_name = "prueba.html"
    context_object_name = "lista_nombres"
