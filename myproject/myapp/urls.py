from django.urls import path


from .views import (
    CustomerProfileListCreateView,
    
    RoomListCreateView,
    RoomDetailView,
    BookingListCreateView,
    BookingDetailsView,
    RegisterView,
    LoginView,
    ProfileView,
    LogoutView
)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    
    #path('register/', RegisterView.as_view(), name='register'),
    
    
    
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path("logout/", LogoutView.as_view()),
    path('profile/', ProfileView.as_view()),
    
    
    
    
    # Customer urls
    path('customers/', CustomerProfileListCreateView.as_view(), name='customer-list-create'),
    #path('customers/<int:pk>/', CustomerProfileDetailView.as_view(), name='customer-detail'),
    
    # Room details urls admin site only
    #path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    #path('rooms/<int:pk>/', RoomDetailView.as_view(), name='room-detail'),
    
    # Booking details urls call api only
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    #path('bookings/<int:pk>/', BookingDetailsView.as_view(), name='booking-detail'),
    
]