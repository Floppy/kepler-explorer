from django.views.generic import ListView, DetailView

from .models import Planet, SolarSystem


class SystemMixin(object):
    model = SolarSystem
    def get_queryset(self):
        return super(SystemMixin, self).get_queryset().filter(radius__isnull=False)


class PlanetMixin(object):
    model = Planet
    def get_queryset(self):
        return super(PlanetMixin, self).get_queryset().filter(
                solar_system__radius__isnull=False,
                radius__isnull=False)


class SystemList(SystemMixin, ListView):
    pass


class SystemDetail(SystemMixin, DetailView):
    pass

class PlanetList(PlanetMixin, ListView):
    pass

class PlanetDetail(PlanetMixin, DetailView):
    pass
