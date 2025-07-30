from django.contrib import admin

from src.sync.models import SyncLogModel


# Register your models here.
@admin.register(SyncLogModel)
class SyncLogAdmin(admin.ModelAdmin):
    list_display = ["run_date", "new_count", "updated_count"]
