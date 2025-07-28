import uuid

from django.db import models

from src.events.models.event_place import EventPlaceModel


class EventModel(models.Model):
    """
    Модель мероприятия
    """

    class Status(models.TextChoices):
        """
        Варианты статусов метоприятия
        """

        OPEN = "open", "Открыто"
        CLOSED = "closed", "Закрыто"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID мероприятия",
    )
    title = models.CharField(max_length=255, verbose_name="Название мероприятия")
    date = models.DateTimeField(verbose_name="Дата проведения мероприятия")
    status = models.CharField(
        max_length=6, choices=Status.choices, verbose_name="Статус мероприятия"
    )
    place = models.ForeignKey(
        EventPlaceModel,
        on_delete=models.SET_NULL,
        related_name="events",
        verbose_name="Место проведения мероприятия",
        null=True,
    )
