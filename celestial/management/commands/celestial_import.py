from django.core.management.base import BaseCommand, CommandError
from celestial.exoplanets_importer import ExoplanetsImporter

class Command(BaseCommand):
    help = 'Import data for celestial objects'

    def handle(self, *args, **options):
        if args:
            ExoplanetsImporter.run(*args)
        else:
            ExoplanetsImporter.run()
        # Import sol data
        ExoplanetsImporter.run("celestial/data/sol.csv")
