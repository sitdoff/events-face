from datetime import datetime

import requests
from django.conf import settings
from django.db import transaction

from src.events.models import EventModel
from src.sync.models import SyncLogModel


class EventSyncService:
    API_URL = settings.API_URL

    def fetch_events(self, changed_at: datetime | None = None) -> dict:
        params = {}
        if changed_at is not None:
            self.API_URL += f"?changed_at={changed_at.strftime('%Y-%m-%d')}"
        print(self.API_URL)
        with requests.get(self.API_URL, params=params) as response:
            response.raise_for_status()
            return response.json()

    def sync(self, changed_at: datetime | None = None) -> tuple[int, int]:
        events = self.fetch_events(changed_at)
        new, updated = 0, 0
        with transaction.atomic():
            for event in events:
                obj, created = EventModel.objects.update_or_create(
                    id=event["id"],
                    defaults={
                        "title": event["title"],
                        "date": event["date"],
                        "status": event["status"],
                        "pace": event["place"],
                    },
                )
                if created is not None:
                    new += 1
                else:
                    updated += 1
            SyncLogModel.objects.create(new=new, updated=updated)
        return new, updated

    def purge(self, days: int = 7) -> None:
        pass
        # EventModel.objects.filter(date__lt=datetime.now() - days).delete()
