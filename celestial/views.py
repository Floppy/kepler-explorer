from django.views.generic import ListView, DetailView

from .models import Planet, SolarSystem


class PlanetList(ListView):
    model = Planet


class PlanetDetail(DetailView):
    model = Planet


class SystemDetail(DetailView):
    model = SolarSystem
