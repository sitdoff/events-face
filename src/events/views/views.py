from rest_framework.pagination import CursorPagination
from rest_framework.request import Request
from rest_framework.views import APIView

from src.events.serializers import EventSerializer
from src.events.services import EventService


class EventsPagination(CursorPagination):
    def __init__(self, ordering="date", page_size: int = 10) -> None:
        self.ordering = ordering
        self.page_size = page_size


class EventsView(APIView):
    def get(self, request: Request, *args, **kwargs):
        service = EventService()
        paginator = EventsPagination(
            page_size=2,
        )
        queryset = service.get_events_page(request)
        page = paginator.paginate_queryset(queryset, request, view=self)
        serializer = EventSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
