from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Collects static files and does migrations.'

    def handle(self, *args, **options):
        call_command('collectstatic', interactive=False)
        call_command('migrate', interactive=False)
