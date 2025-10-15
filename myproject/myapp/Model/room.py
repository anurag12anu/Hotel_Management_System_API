from django.db import models

class Room(models.Model):
    ROOM_TYPE=[
        ('Single','Sigle'),
        ('Double','Double'),
        ('Suite','Suite'),
    ]
    number=models.CharField(max_length=10, unique=True)
    room_type=models.CharField(max_length=10,choices=ROOM_TYPE)
    price_per_night=models.DecimalField(max_digits=10,decimal_places=2)
    is_available=models.BooleanField(default=True)
    
    def __str__(self):
        return f"Room {self.number} ({self.room_type})"
