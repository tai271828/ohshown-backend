from django.db import models

from .mixins import SoftDeleteMixin
from .ohshown_event import OhshownEvent

from users.models import CustomUser


class Review(SoftDeleteMixin):

    reviewer = models.ForeignKey(
        CustomUser,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="reviews",
    )
    factory = models.ForeignKey(
        OhshownEvent,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    reason = models.TextField(help_text="")
