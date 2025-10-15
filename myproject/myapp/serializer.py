from .Model.Booking import Booking
from .Model.room import Room
from .Model.customer import CustomerProfile

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields='__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'
class CustomerSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(read_only=True)
    class Meta:
        model=CustomerProfile
        fields='__all__'
        
