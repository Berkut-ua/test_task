from rest_framework import serializers

from test_task.models import Reservation


class ReservationsSerializer(serializers.ModelSerializer):
    rental_name = serializers.CharField(source='rental.name')
    prev_reservation_id = serializers.CharField(source='prev')
    
    class Meta:
        model = Reservation
        fields = ['rental_name', 'id', 'checkin', 'checkout', 'prev_reservation_id']
