from django.contrib import admin
from myapp.Model.room import Room
from myapp.Model.customer import CustomerProfile
from myapp.Model.Booking import Booking
from django.contrib.auth.models import User


admin.site.register(Room)
admin.site.register(CustomerProfile)
admin.site.register(Booking)

