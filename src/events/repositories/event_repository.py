from django.db.models import QuerySet

from src.events.models import EventModel


class EventRepository:
    """
    Репозиторий для работы с EventModel
    """

    model = EventModel

    def get_all(self) -> QuerySet[EventModel]:
        queryset = self.model.objects.select_related("place").all()
        return queryset

    def get_all_open_events(self) -> QuerySet[EventModel]:
        queryset = self.get_all().filter(status=EventModel.Status.OPEN)
        return queryset
