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
    def get_context_data(self, **kwargs):
        data = super(SystemDetail, self).get_context_data(**kwargs)
        data.update({'planets': Planet.objects.filter(solar_system=self.object, radius__isnull=False).order_by('semi_major_axis')})
        return data


class PlanetList(PlanetMixin, ListView):
    pass


class PlanetDetail(PlanetMixin, DetailView):
    pass
