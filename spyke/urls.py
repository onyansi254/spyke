# urls.py

from django.urls import path
from location.views import display_location
from django.contrib import admin  
from django.urls import path, include

urlpatterns = [
    path('location/', display_location, name='display_location'),
     path('admin/', admin.site.urls),
    path('location/', include('location.urls')),
]
