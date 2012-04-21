import factory
from decimal import Decimal
from django.test import TestCase

from .models import SolarSystem, Planet


class SolarSystemFactory(factory.Factory):
    FACTORY_FOR = SolarSystem
    name = factory.Sequence(lambda n: 'System {0}'.format(n))
    distance =  Decimal("56.2746186965")
    right_ascension =  Decimal("19.9041172221")
    magnitude =  Decimal("4.7100000381")
    declination =  Decimal("8.4616499996")
    radius = Decimal("0.01")
    temperature = "4780"


class PlanetFactory(factory.Factory):
    FACTORY_FOR = Planet
    name = factory.Sequence(lambda n: 'Planet roduct {0}'.format(n))
    solar_system = factory.SubFactory(SolarSystemFactory)
    semi_major_axis =  Decimal("0.6758886576")
    gravity =  Decimal("10.0")
    orbital_period =  Decimal("136.75")
    radius = Decimal("1.5")
    temperature =  "42"

class PlanetTest(TestCase):

    def setUp(self):
        self.planet = PlanetFactory()
 
    def test_stats(self):
        """
        Tests stats produce sensible numbers.
        """
        self.assertEqual(self.planet.time_to_go_circumnavigate_by_airbus_a380, Decimal('0.03769911184307751739197556162'))
        self.assertEqual(self.planet.time_to_planet_by_spacecraft, Decimal('100631610615981.6203852879867'))
        self.assertEqual(self.planet.time_to_planet_by_car, Decimal('55490553574007693.66724963385'))
        self.assertEqual(self.planet.size_of_star_in_sky, Decimal(9.872222471748167e-08))
        self.assertEqual(self.planet.colour_of_star, '#9bb0ff')
        self.assertEqual(self.planet.weight_on_planet(5.0), Decimal('5.098581064889641512818435200'))
        self.assertEqual(self.planet.age_in_planet_years(5), Decimal('1.871972864166092458898227719'))
