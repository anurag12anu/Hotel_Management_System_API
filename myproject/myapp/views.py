from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions

from .serializer import CustomerSerializer,BookingSerializer,RoomSerializer,UserSerializer

from .Model.Booking import Booking
from .Model.room import Room
from .Model.customer import CustomerProfile

class CustomerProfileListCreateView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        profiles =CustomerProfile.objects.all()
        serializer=CustomerSerializer(profiles, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user) # link customer profile with logged in user
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomerProfileDetailView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self, pk ):
        try:
            return CustomerProfile.objects.get(pk=pk)
        except CustomerProfile.DoesNotExist:
            return None
    def get(self,request,pk):
        
        profile=self.get_object(pk)
        if not profile:
            return Response({'errors':'customer profile not find'}, status=status.HTTP_404_NOT_FOUND)
        serializer=CustomerSerializer(profile)
        return Response(serializer.data)
    
    def put(self, request,pk):
        profile=self.get_object(pk)
        if not profile:
            return Response({'errors':'customer profile not find'}, status=status.HTTP_404_NOT_FOUND)
        serializer =CustomerSerializer(profile, request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, requsest,pk):
        profile=self.get_object(pk)
        if not profile:
            return Response({'errors':'customer profile not find'}, status=status.HTTP_404_NOT_FOUND)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
            
