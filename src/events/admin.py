from django.contrib import admin

from src.events.models import EventModel, EventPlaceModel

# Register your models here.


@admin.register(EventModel)
class EventAdmin(admin.ModelAdmin):
    verbose_name = "Мероприятие"
    verbose_name_plural = "Мероприятия"
    list_display = ["title", "date", "status", "place"]
    list_filter = ["status", "place"]
    search_fields = ["title", "place__title"]


@admin.register(EventPlaceModel)
class EventPlaceAdmin(admin.ModelAdmin):
    verbose_name = "Место проведения мероприятия"
    verbose_name_plural = "Места проведения мероприятия"
    list_display = ["title"]
