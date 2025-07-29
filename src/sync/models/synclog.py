from django.db import models


class SyncLogModel(models.Model):
    run_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата синхронизации"
    )
    new_count = models.PositiveIntegerField(verbose_name="Количество новых ивентов")
    updated_count = models.PositiveIntegerField(
        verbose_name="Количество обновленных ивентов"
    )
