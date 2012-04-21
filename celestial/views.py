from django.views.generic import ListView, DetailView

from .models import Planet, SolarSystem


class SystemList(ListView):
    model = SolarSystem


class SystemDetail(DetailView):
    model = SolarSystem


class PlanetList(ListView):
    model = Planet
    
    def get_queryset(self):
        return super(PlanetList, self).get_queryset().filter(radius__isnull = False)


class PlanetDetail(DetailView):
    model = Planet
