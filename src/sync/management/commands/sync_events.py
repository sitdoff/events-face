from datetime import datetime, timedelta

from django.core.management import BaseCommand
from requests.exceptions import SSLError

from src.sync.services import EventSyncService


class Command(BaseCommand):
    """
    Команда для запуска синхронизации мероприятий.
    """

    help = "Sync events from API"

    def add_arguments(self, parser):
        parser.add_argument(
            "--date",
            type=str,
            help="Синхронизировать за дату YYYY-MM-DD",
        )
        parser.add_argument(
            "--all",
            action="store_true",
            help="Синхронизировать все мероприятия",
        )

    def handle(self, *args, **options):
        service = EventSyncService()
        if options.get("all"):
            changed = None
        else:
            if date := options.get("date"):
                changed = datetime.fromisoformat(date)
            else:
                changed = datetime.now().date() - timedelta(days=1)
        try:
            new, updated = service.sync(changed)
            self.stdout.write(
                self.style.SUCCESS(f"Synced Events. New: {new}, Updated: {updated}.")
            )
        except SSLError as exc:
            self.stdout.write(self.style.ERROR(f"Sync Events Error. {exc}"))
