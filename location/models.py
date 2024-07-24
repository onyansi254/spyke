from django.db import models

# Create your models here.


from django.db import models

class Location(models.Model):
    phone_number = models.CharField(max_length=15)  # Field for the phone number
    latitude = models.FloatField(null=True, blank=True)  # Latitude of the location
    longitude = models.FloatField(null=True, blank=True)  # Longitude of the location
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp when the location was saved

    def __str__(self):
        return f"{self.phone_number} - Lat: {self.latitude}, Lon: {self.longitude}"
