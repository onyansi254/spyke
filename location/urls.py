from django.urls import path
from .views import track_location, location_detail, location_data, display_location

urlpatterns = [
    path('track/', track_location, name='track_location'),  # tracking phone number
    path('location/<int:pk>/', location_detail, name='location_detail'),  # viewing location details
    path('location/<int:pk>/data/', location_data, name='location_data'),  # real-time location updates
    path('display-location/', display_location, name='display_location'),
]
