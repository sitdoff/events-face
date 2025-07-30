from rest_framework import serializers

from src.events.models import EventModel


class EventSerializer(serializers.ModelSerializer):
    place = serializers.CharField(source="place.title", read_only=True)

    class Meta:
        model = EventModel
        fields = [
            "id",
            "name",
            "event_time",
            "registration_deadline",
            "status",
            "place",
        ]
