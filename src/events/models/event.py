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

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID мероприятия",
    )
    name = models.CharField(max_length=255, verbose_name="Название мероприятия")
    event_time = models.DateTimeField(verbose_name="Дата проведения мероприятия")
    registration_deadline = models.DateTimeField(
        verbose_name="Дата окончания регистрации"
    )
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

    def __str__(self) -> str:
        return f"{self.name} - {self.event_time}"
