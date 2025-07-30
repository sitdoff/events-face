from django.db.models import QuerySet
from rest_framework.request import Request

from src.events.models import EventModel
from src.events.repositories import EventRepository


class EventService:
    """
    Сервис для операций с EventModel
    """

    def __init__(
        self,
        event_repository: EventRepository = EventRepository(),
    ):
        self.event_repository = event_repository

    def get_all(self):
        """
        Получение всех EventModel
        """
        queryset = self.event_repository.get_all()
        return queryset

    def filter(self, queryset, **kwargs) -> QuerySet[EventModel]:
        """
        Фильтрация EventModel
        """
        return queryset.filter(**kwargs)

    def ordering(self, queryset, order_by: str) -> QuerySet[EventModel]:
        """
        Сортировка по указаному полю
        """
        return queryset.order_by(order_by)

    def get_events(self, request: Request, **kwargs) -> QuerySet[EventModel]:
        """
        Получает EventModel с фильтрацией по полю имени
        """
        queryset = self.event_repository.get_all_open_events()
        if (name := request.query_params.get("name")) is not None:
            queryset = self.filter(queryset, name__icontains=name)
        return queryset
