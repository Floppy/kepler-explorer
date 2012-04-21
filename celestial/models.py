from django.db import models
from django.utils.translation import ugettext_lazy as _

class SolarSystem(models.Model):
    """
    A star is a massive, luminous sphere of plasma held together by gravity.
    """
    name = models.CharField(max_length=64, unique=True,
            help_text=_('Name for primary star'))
    magnitude = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True,
            help_text=_('Magnitude'))
    radius = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True,
            help_text=_('Radius of primary star'))
    temperature = models.IntegerField(null=True, blank=True,
            help_text=_('Surface temperature of star'))
    right_ascension = models.CharField(max_length=32,
            help_text=_('Right Ascension'))
    declination = models.CharField(max_length=32,
            help_text=_('Declination'))
    distance = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True,
            help_text=_('Distance from Earth'))

    class Meta:
        verbose_name = 'Solar System'
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('system-detail', [self.pk])


class Planet(models.Model):
    """A planet is a celestial body orbiting a star"""
    name = models.CharField(max_length=255, unique=True)
    solar_system = models.ForeignKey('celestial.SolarSystem', related_name='planets')
    radius = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True,
            help_text=_('Planetary radius in Earth radii (6378 km) Product of r/R* and the stellar radius'))
    temperature = models.IntegerField(null=True, blank=True,
            help_text=_('Equilibrium surface temperature of planet'))
    semi_major_axis = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True,
            help_text=_('''Semi-major axis of orbit in AU based on Newton's generalization of Kepler's third law'''))

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('planet-detail', [self.pk])
