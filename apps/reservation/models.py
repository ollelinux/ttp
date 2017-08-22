from django.db import models
from django.utils import timezone

from ..form_field import FixedCharField


class Reservation(models.Model):
    first_name = models.CharField(max_length=255, db_index=True)
    last_name = models.CharField(max_length=255, db_index=True)
    room = models.CharField(max_length=200, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"The room {self.room} is booked by {self.first_name} {self.last_name}"
