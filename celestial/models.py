from django.db import models
from django.utils.translation import ugettext_lazy as _
from math import pi, atan2
from decimal import Decimal

class SolarSystem(models.Model):
    """
    A star is a massive, luminous sphere of plasma held together by gravity.
    """
    name = models.CharField(max_length=64, unique=True,
            help_text=_('Name for primary star'))
    magnitude = models.DecimalField(max_digits=14, decimal_places=10, null=True, blank=True,
            help_text=_('Magnitude'))
    radius = models.DecimalField(max_digits=14, decimal_places=10, null=True, blank=True,
            help_text=_('Radius of primary star'))
    temperature = models.DecimalField(max_digits=14, decimal_places=10, null=True, blank=True,
            help_text=_('Surface temperature of star'))
    right_ascension = models.CharField(max_length=32,
            help_text=_('Right Ascension'))
    declination = models.CharField(max_length=32,
            help_text=_('Declination'))
    distance = models.DecimalField(max_digits=14, decimal_places=10, null=True, blank=True,
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
    radius = models.DecimalField(max_digits=14, decimal_places=10, null=True, blank=True,
            help_text=_('Planetary radius in Earth radii (6378 km) Product of r/R* and the stellar radius'))
    temperature = models.DecimalField(max_digits=14, decimal_places=10, null=True, blank=True,
            help_text=_('Equilibrium surface temperature of planet'))
    semi_major_axis = models.DecimalField(max_digits=14, decimal_places=10, null=True, blank=True,
            help_text=_('''Semi-major axis of orbit in AU based on Newton's generalization of Kepler's third law'''))
    # TODO these need to be real
    gravity = 10 # m/s
    orbital_period = 365 # days

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('planet-detail', [self.pk])

    def weight_on_planet(self, weight_on_earth):
        """
        Calculates how much something would weigh on a planet with a given gravity

        weight_on_earth - the weight of the object on earth (in unspecified units)
        planet_gravity - acceleration due to gravity on the planet

        returns the weight of the object on the planet, in the same units it was given in
        """

        return weight_on_earth * (self.gravity / 9.80665)

    @property
    def time_to_go_circumnavigate_by_airbus_a380(self):
        """
        Calculates the time taken to circumnavigate a planet using an Airbus A380
        (travelling at 900km/h)

        planet_radius - radius of the planet in m

        returns the time in seconds to circumnavigate the planet
        """

        # 900 km/h = 250 m/s
        circ = Decimal(2*pi) * self.radius
        return circ/Decimal(250.0)

    def age_in_planet_years(self, age_in_years):
        """
        Calculates how old you would be if you lived on an exo-planet

        age_in_years - the age on Earth, in years
        planetary_orbit_period - the planetary orbital period, in days

        returns the age in planet years, i.e. how many times the planet has
        orbitted its star in the time given
        """
        return age_in_years * self.orbital_period / 365.256363

    def time_to_planet_at_speed(self, speed_of_craft):
        m_per_parsec = 3.08568025e16
        if not self.solar_system.distance:
            return ''
        return self.solar_system.distance * m_per_parsec / speed_of_craft


    @property
    def time_to_planet_by_spacecraft(self):
        """
        Calculates the time to travel to the planet by spacecraft
        This assumes a travelling speed of 62,120km/h (17255.5 m/s), which is the solar
        system espace velocity of Voyager 1

        planet_distance - the distance to the planet in parsecs

        returns the time in seconds taken to get to the planet
        """
        speed_of_craft = 17255.56
        return self.time_to_planet_at_speed(speed_of_craft)

    @property
    def time_to_planet_by_car(self):
        """
        Calculates the time to travel to the planet by car
        This assumes a travelling speed of 31.2928m/s (70mph), which is the
        speed limit in the UK

        planet_distance - the distance to the planet in parsecs

        returns the time in seconds taken to get to the planet
        """
        speed_of_craft = 31.2928
        return self.time_to_planet_at_speed(speed_of_craft)

    @property
    def size_of_star_in_sky(self):
        """
        Calculates the size of the star in the sky from the surface of the planet

        star_radius - radius of the star
        star_distance - distance to the star

        units of radius and distance are unimportant, but must be the same

        returns the size of the star in the sky in degrees
        """

        if not self.solar_system.radius:
            return ''
        if not self.solar_system.distance:
            return ''

        # Radius is in AU, so convert to km
        radius = self.solar_system.radius * 149598000
        # Distance is in parsecs, so convert to km
        distance = self.solar_system.distance * 3.08568025e13

        # 2* because we only give radius (not diameter), 180/pi to convert to degrees
        return 2*atan2(radius, distance)*180/pi

    @property
    def colour_of_star(self):
        """
        Calculates the colour of the star based on its temperature

        temperature - the temperature of the star in K

        returns a string representing the HTML colour of the star
        """
        # Colours based on data here:
        # http://outreach.atnf.csiro.au/education/senior/astrophysics/photometry_colour.html
        temperature = self.solar_system.temperature

        if (temperature > 28000):
            return "#9bb0ff"
        elif (temperature > 10000):
            return "#aabfff"
        elif (temperature > 7500):
            return "#cad7ff"
        elif (temperature > 6000):
            return "#f8f7ff"
        elif (temperature > 4900):
            return "#fff4ea"
        elif (temperature > 3500):
            return "#ffd2a1"
        else:
            return "#ffccdf"
