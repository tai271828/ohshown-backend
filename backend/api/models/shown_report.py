import uuid

from django.db import models

from .mixins import SoftDeleteMixin


class ShownReport(SoftDeleteMixin):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID",
    )
    # TODO reporter FK
    # TODO reference 子表單
    lat = models.FloatField()
    lng = models.FloatField()
    datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
