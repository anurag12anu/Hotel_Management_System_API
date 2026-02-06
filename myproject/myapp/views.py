from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions

from .serializer import CustomerSerializer,BookingSerializer,RoomSerializer,RegisterSerializer,LoginSerializer

from .Model.Booking import Booking
from .Model.room import Room
from .Model.customer import CustomerProfile

from rest_framework.permissions import AllowAny

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {'message': 'User registered successfully'},
            status=status.HTTP_201_CREATED
        )



class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)
    
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email
        })
        

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"message": "Logged out successfully"},
                status=status.HTTP_205_RESET_CONTENT
            )
        except Exception:
            return Response(
                {"error": "Invalid refresh token"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        
class CustomerProfileListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        profile = CustomerProfile.objects.filter(users=request.user)
        serializer = CustomerSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomListCreateView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        room_data=Room.objects.all()
        serializer=RoomSerializer(room_data,many=True)
        return Response(serializer.data)
    

class RoomDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self,pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            return None
    
    def get(self,request,pk):
        room=self.get_object(pk)
        if room is None:
            return Response({'errors','Room not found'},status=404)
        
        serializer=RoomSerializer(room)
        
        return Response(serializer.data)
    



class BookingListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        customer = CustomerProfile.objects.get(users=request.user)
        bookings = Booking.objects.filter(userss=customer)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookingSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            # serializer.create() will handle room_number_write -> room
            booking = serializer.save()

            # Check for overlapping bookings AFTER we have the room object
            if Booking.objects.filter(
                room=booking.room,
                check_out__gte=booking.check_in,
                check_in__lte=booking.check_out
            ).exclude(id=booking.id).exists():
                booking.delete()  # remove conflicting booking
                return Response(
                    {"error": "Room is already booked for selected dates"},
                    status=400
                )

            return Response(
                BookingSerializer(booking).data,
                status=201
            )

        return Response(serializer.errors, status=400)



class BookingDetailsView(APIView):
    permission_classes = [AllowAny]
    
    
    def get_object(self,request,pk):
        try:
        
            bookings=Booking.objects.get(pk=pk)
            
        except Booking.DoesNotExist:
            return None
    
    def get(self,request,pk):
        booking=self.get_object(pk)
        
        if booking is None:
            return Response({'errors',' Booking not found'})
        
        serializer=BookingSerializer(booking)
        return Response(serializer.data)
    
    def put(self,request,pk):
        
        booking=self.get_object(pk)
        serializer=BookingSerializer(booking)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=404)
    
    def delete(self,request,pk):
        booking=self.get_object(pk)
        
        if booking is None:
            return Response({'errors':'Booking not found'},status=status.HTTP_404_NOT_FOUND)
        
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
             
