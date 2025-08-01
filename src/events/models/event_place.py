import uuid

from django.db import models


class EventPlaceModel(models.Model):
    """
    Место проведения мероприятия
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Название места проведения")

    class Meta:
        verbose_name = "Место проведения мероприятия"
        verbose_name_plural = "Места проведения мероприятий"

    def __str__(self) -> str:
        return f"{self.name}"
