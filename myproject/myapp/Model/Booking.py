from django.db import models
from django.contrib.auth.models import User
from .room import Room

class Booking(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in=models.DateField()
    total_price=models.DecimalField(max_digits=8,decimal_places=2)
    booked_on=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"
    

