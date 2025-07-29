from django.db.models import QuerySet
from rest_framework.request import Request

from src.events.models import EventModel
from src.events.repositories import EventRepository


class EventService:
    def __init__(
        self,
        event_repository: EventRepository = EventRepository(),
    ):
        self.event_repository = event_repository

    def get_all(self):
        queryset = self.event_repository.get_all()
        return queryset

    def filter(self, queryset, **kwargs) -> QuerySet[EventModel]:
        return queryset.filter(**kwargs)

    def ordering(self, queryset, order_by: str) -> QuerySet[EventModel]:
        return queryset.order_by(order_by)

    def get_events_page(self, request: Request, **kwargs) -> QuerySet[EventModel]:
        queryset = self.event_repository.get_all_open_events()
        if (title := request.query_params.get("title")) is not None:
            queryset = self.filter(queryset, title__icontains=title)
        return queryset
