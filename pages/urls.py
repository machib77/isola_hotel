from django.urls import path
from .views import (
    HomePageView,
    ContactoPageView,
    HabitacionesPageView,
    De_LujoPageView,
    GrupalPageView,
    TriplePageView,
    DoblePageView,
    SimplePageView,
    GastronomiaPageView,
    ExperienciasPageView,
)

from django.contrib.sitemaps.views import sitemap  # Para sitemaps
from .sitemaps import StaticSitemap  # Para sitemaps

# Para sitemaps
sitemaps = {
    "static": StaticSitemap,
}

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("contacto/", ContactoPageView.as_view(), name="contacto"),
    path("habitaciones/", HabitacionesPageView.as_view(), name="habitaciones"),
    path("habitaciones/de_lujo/", De_LujoPageView.as_view(), name="de_lujo"),
    path("habitaciones/grupal/", GrupalPageView.as_view(), name="grupal"),
    path("habitaciones/triple/", TriplePageView.as_view(), name="triple"),
    path("habitaciones/doble/", DoblePageView.as_view(), name="doble"),
    path("habitaciones/simple/", SimplePageView.as_view(), name="simple"),
    path("gastronomia/", GastronomiaPageView.as_view(), name="gastronomia"),
    path("experiencias/", ExperienciasPageView.as_view(), name="experiencias"),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
