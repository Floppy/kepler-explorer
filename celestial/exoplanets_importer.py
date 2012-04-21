import requests
import csv
from models import Planet, SolarSystem
from django.core.exceptions import ValidationError

class ExoplanetsImporter:
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
                    system.temperature = row[headers['TEFF']] or None
                    system.save()
                except ValidationError:
                    print stardata
                    raise
                # Find and store planet data
                try:
                    planet, created = Planet.objects.get_or_create(name = row[headers['NAME']], solar_system = system)
                    planet.radius = row[headers['R']] or None
                    planet.semi_major_axis = row[headers['A']]
                    planet.save()
                except ValidationError:
                    print planetdata
                    raise
