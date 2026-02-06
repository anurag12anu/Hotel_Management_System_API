from django.db import models
from django.contrib.auth.models import User
from .customer import CustomerProfile
from .room import Room
import datetime

class Booking(models.Model):
    userss = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    booked_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        
        nights = (self.check_out - self.check_in).days

        if nights <= 0:
            nights = 1  

        
        self.total_price = self.room.price_per_night * nights

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking by {self.userss.users.username} - Room {self.room.number}"
    

