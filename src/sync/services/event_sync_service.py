from datetime import datetime

import pybreaker
import redis
import requests
from django.conf import settings
from django.db import transaction

from src.events.models import EventModel
from src.sync.models import SyncLogModel

redis = redis.StrictRedis(
    host="localhost",
    port=6379,
    db=10,
)
breaker = pybreaker.CircuitBreaker(
    fail_max=2,
    reset_timeout=60,
    state_storage=pybreaker.CircuitRedisStorage(pybreaker.STATE_CLOSED, redis),
)


class EventSyncService:
    """
    Сервис для синхронизации мероприятий co сторонним API.
    """

    API_URL = settings.API_URL

    @breaker
    def fetch_events(self, changed_at: datetime | None = None) -> dict:
        """
        Делает запрос на сторонний API.
        """
        if changed_at is not None:
            self.API_URL += f"?changed_at={changed_at.strftime('%Y-%m-%d')}"
        with requests.get(self.API_URL) as response:
            response.raise_for_status()
            return response.json()

    def sync(self, changed_at: datetime | None = None) -> tuple[int, int]:
        """
        Записывает объекты мероприятия в базу данных.
        """
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
