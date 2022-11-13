from django.db import models

class Rental(models.Model):
    name = models.CharField(default='', max_length=20)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE,
                               related_name='rental_reservations')
    checkin = models.DateField(null=False)
    checkout = models.DateField(null=False)
