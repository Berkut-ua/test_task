from rest_framework import generics
from django.db.models import Window
from django.db.models.functions import Lag

from test_task.serializers import ReservationsSerializer

from test_task.models import Reservation


class Reservations(generics.ListAPIView):
    serializer_class = ReservationsSerializer

    def get_queryset(self):
        # select r.name, res.id, res.checkin, res.checkout, LAG(res.id, 1, "-") OVER (PARTITION BY res.rental_id ORDER BY res.id) as prev from test_task_reservation as res join test_task_rental as r on r.id=res.rental_id;
        reservation_before_by_date = Reservation.objects.all().annotate(prev=Window(expression=Lag('id'), partition_by='rental_id', order_by='checkout'))
        return reservation_before_by_date
