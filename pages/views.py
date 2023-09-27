from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class ContactoPageView(TemplateView):
    template_name = "contacto.html"


class HabitacionesPageView(TemplateView):
    template_name = "habitaciones.html"


class De_LujoPageView(TemplateView):
    template_name = "de_lujo.html"


class GrupalPageView(TemplateView):
    template_name = "grupal.html"


class TriplePageView(TemplateView):
    template_name = "triple.html"


class DoblePageView(TemplateView):
    template_name = "doble.html"


class SimplePageView(TemplateView):
    template_name = "simple.html"


class GastronomiaPageView(TemplateView):
    template_name = "gastronomia.html"


class ExperienciasPageView(TemplateView):
    template_name = "experiencias.html"


class ImagenesPageView(TemplateView):
    template_name = "imagenes.html"


class VideosPageView(TemplateView):
    template_name = "videos.html"
