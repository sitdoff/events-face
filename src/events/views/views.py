from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView

from src.events.paginators import EventsPagination
from src.events.serializers import EventSerializer
from src.events.services import EventService


class EventsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request, *args, **kwargs):
        service = EventService()
        paginator = EventsPagination()
        queryset = service.get_events_page(request)
        page = paginator.paginate_queryset(queryset, request, view=self)
        serializer = EventSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
