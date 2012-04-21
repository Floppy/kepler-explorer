from django.views.generic import ListView, DetailView

from .models import Planet, SolarSystem


class SystemList(ListView):
    model = SolarSystem


class SystemDetail(DetailView):
    model = SolarSystem


class PlanetList(ListView):
    model = Planet


class PlanetDetail(DetailView):
    model = Planet
