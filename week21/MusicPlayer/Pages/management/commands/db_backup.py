from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Database Back up"

    def handle(self, *args, **options):
        backup_file = 'backup.json'
        with open(f"backups/{backup_file}", "w") as f:
            call_command('dumpdata', stdout=f)

        self.stdout.write(self.style.SUCCESS('Database backup was created successfully'))
