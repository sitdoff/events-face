from django.db.models import QuerySet

from src.events.models import EventModel


class EventRepository:
    """
    Репозиторий для работы с EventModel
    """

    model = EventModel

    def get_all(self) -> QuerySet[EventModel]:
        queryset = self.model.objects.all()
        return queryset

    def get_all_open_events(self) -> QuerySet[EventModel]:
        queryset = self.get_all()
        queryset = queryset.filter(status=EventModel.Status.OPEN)
        return queryset

    def join_event_place(self, queryset: QuerySet[EventModel]) -> QuerySet[EventModel]:
        return queryset.select_related("place")
