from .Model.Booking import Booking
from .Model.room import Room
from .Model.customer import CustomerProfile



from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email','password' ]

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['username'],
            password=data['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.id,
            'username': user.username,
        }



class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields='__all__'

class BookingSerializer(serializers.ModelSerializer):
    booked_by = serializers.SerializerMethodField()
    room_number = serializers.IntegerField(source='room.number', read_only=True)
    room_number_write = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Booking
        fields = [
            'id', 'room_number', 'room', 'check_in', 'check_out',
            'total_price', 'booked_on','room_number_write', 'booked_by'
        ]
        read_only_fields = ['room', 'total_price', 'booked_on', 'booked_by']

    def get_booked_by(self, obj):
        return {
            "first_name": obj.userss.first_name,
            "last_name": obj.userss.last_name,
            "email": obj.userss.users.email,
            "username": obj.userss.users.username
        }

    # Optional: If you want to allow POST using room_number instead of room ID
    room_number_write = serializers.IntegerField(write_only=True, required=False)

    def create(self, validated_data):
        customer = self.context['request'].user.customerprofile  # get current user's CustomerProfile

        room_number = validated_data.pop('room_number_write', None)
        if room_number:
            try:
                room = Room.objects.get(number=room_number)
                validated_data['room'] = room
            except Room.DoesNotExist:
                raise serializers.ValidationError("Room with this number does not exist.")

        validated_data['userss'] = customer
        return super().create(validated_data)
        
class CustomerSerializer(serializers.ModelSerializer):
    users = RegisterSerializer(read_only=True)
    class Meta:
        model = CustomerProfile
        fields = ['id', 'users','first_name', 'last_name', 'phone', 'address']
        read_only_fields = ['users']

    def create(self, validated_data):
        request = self.context['request']
        validated_data['users'] = request.user   # ✅ correct field name
        return CustomerProfile.objects.create(**validated_data)


        
