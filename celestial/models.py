from django.db import models
from django.utils.translation import ugettext_lazy as _

class SolarSystem(models.Model):
    """
    A star is a massive, luminous sphere of plasma held together by gravity.
    magnitude
    temperature
    radius
    """
    kepler_id = models.CharField(max_length=32,
            help_text=_('Kepler ID for host star from Kepler Input Catalog'))
    magnitude = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True,
            help_text=_('Kepler magnitude'))
    radius = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True,
            help_text=_('Planetary radius in Earth radii (6378 km) Product of r/R* and the stellar radius'))
    temperature = models.IntegerField(null=True, blank=True,
            help_text=_('Equilibrium surface temperature of planet'))
    semi_major_axis = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True,
            help_text=_('''Semi-major axis of orbit in AU based on Newton's generalization of Kepler's third law'''))

    class Meta:
        verbose_name = 'System'
        ordering = ('kepler_id',)

    def __unicode__(self):
        return self.kepler_id

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('view_or_url_name' )


class Planet(models.Model):
    """A planet is a celestial body orbiting a star"""
    name = models.CharField(max_length=255)
    solar_system = models.ForeignKey('celestial.SolarSystem', related_name='planets')

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('planet-detail', [str(self.id)])
