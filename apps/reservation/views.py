from rest_framework import viewsets, generics

from .serializers import ReservationSerializer
from .models import Reservation


class ReservationViewSet(viewsets.ModelViewSet):
    """
    get:
    Return a list of all the existing reservation records.

    post:
    Create a new reservation.
    """
    queryset = Reservation.objects.all().order_by('-created_at')
    serializer_class = ReservationSerializer

    def get_queryset(self):
        """
        Example of query
        http://127.0.0.1:8000/api/reservations/?start_date=2017-10-10T10:00:00Z&end_date=2017-10-14T10:10:00Z
        """
        queryset = super(ReservationViewSet, self).get_queryset()
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(start_date__range=(start_date, end_date))
        return queryset


class ReservationFilter(generics.ListAPIView):
    """
        get:
        Return a list of filtered reservations.
        """
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all().order_by('-created_at')

    def get_queryset(self):
        """
        Example of query
        http://127.0.0.1:8000/api/reservation-filter/2017-10-10T10:00:00Z/2017-10-14T10:10:00Z/
        """
        queryset = super(ReservationFilter, self).get_queryset()
        start_date = self.kwargs['start_date']
        end_date = self.kwargs['end_date']
        if start_date and end_date:
            queryset = queryset.filter(start_date__range=(start_date, end_date))
        return queryset
