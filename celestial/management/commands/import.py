from django.core.management.base import BaseCommand, CommandError
from celestial.exoplanets_importer import ExoplanetsImporter

class Command(BaseCommand):
    help = 'Import data'

    def handle(self, *args, **options):
        ExoplanetsImporter.run()
