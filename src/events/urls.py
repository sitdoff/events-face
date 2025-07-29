from django.urls import path

from src.events.views import EventsView

urlpatterns = [
    path("events", EventsView.as_view(), name="events"),
]
