from decimal import Decimal
import requests
import csv
from math import pi
from models import Planet, SolarSystem
from django.core.exceptions import ValidationError

from .physcon import sigma

class ExoplanetsImporter(object):
    @staticmethod
    def run(filename = None):
        if filename!=None:
            csv_data = open(filename)
        else:
            csv_data = requests.get('http://exoplanets.org/exoplanets.csv')
        rows = csv.reader(csv_data)
        headers = {}
        got_headers = False
        for row in rows:
            if got_headers == 0:
                # Store headers
                colnum = 0
                for col in row:
                    headers[col] = colnum
                    colnum += 1
                got_headers = True
            else:
                # Find and store system data
                try:
                    system, created = SolarSystem.objects.get_or_create(name = row[headers['STAR']])
                    system.magnitude = row[headers['V']] or None
                    try:
                        system.radius = float(row[headers['A']]) / float(row[headers['AR']])
                    except ValueError:
                        system.radius = None
                    system.temperature = row[headers['TEFF']] or None
                    system.right_ascension = row[headers['RA']] or None
                    system.declination = row[headers['DEC']] or None
                    system.distance = row[headers['DISTANCE']] or None
                    system.save()
                except ValidationError:
                    raise
                # Find and store planet data
                try:
                    planet, created = Planet.objects.get_or_create(name = row[headers['NAME']], solar_system = system)
                    planet.radius = row[headers['R']] or None
                    planet.semi_major_axis = row[headers['A']]
                    planet.density = row[headers['DENSITY']] or None
                    planet.temperature = 42 # Obviously not real at the moment
                    if system.radius and system.magnitude and system.temperature and planet.semi_major_axis:
                        piD = Decimal(pi)
                        sigmaD = Decimal(sigma)
                        # AU in kilometers
                        AU = Decimal('149597870.7')
                        # Stella radius (AU)
                        R = Decimal(system.radius)
                        # Distance from planet to star (AU)
                        D = Decimal(planet.semi_major_axis)
                        # Effective temperature of star (Kelvin)
                        T = Decimal(system.temperature)
                        # Luminosity (4*pi*R^2*sigma*T^4)
                        L = 4*piD*R**2*sigmaD*T**4
                        print '%s luminosity: %s' % (system.name, L)
                        # albedo - 1 means that all the radiation is reflected, an albedo of 0 means all of it is absorbed
                        A = Decimal('0.34')
                        # sigma = Constant of proportionality (also Stefan's constant), is the constant of proportionality in the Stefan-Boltzmann law: 
                        #   The total energy radiated per unit surface area of a black body in unit time is proportional to 
                        #   the fourth power of the thermodynamic temperature.

                        planet.temperature = pow((L*(1 - A) / 16*piD*sigmaD*D**2), Decimal(1.0)/4)
                        print '  %s temperature: %s' % (planet.name, planet.temperature)
                    try:
                        planet.gravity = pow(10, float(row[headers['GRAVITY']])) / 100.0 # To get m/s^2
                    except ValueError:
                        system.gravity = None
                    planet.orbital_period = row[headers['PER']]
                    planet.save()
                except ValidationError:
                    raise
