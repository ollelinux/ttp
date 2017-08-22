from rest_framework import serializers

from .models import Reservation


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = ('first_name', 'last_name', 'room', 'start_date', 'end_date')
