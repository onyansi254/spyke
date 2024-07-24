from django.shortcuts import render
from django.http import HttpResponse
import requests
import folium
import datetime
import os

def locationCoordinates():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        return lat, long, city, state
    except:
        return None, None, 'Error', 'Error'

def gps_locator():
    obj = folium.Map(location=[0, 0], zoom_start=2)
    try:
        lat, long, city, state = locationCoordinates()
        if lat is None:
            return None
        folium.Marker([lat, long], popup='Current Location').add_to(obj)
        fileName = os.path.join("static", "Location_" + str(datetime.date.today()) + ".html")
        obj.save(fileName)
        return fileName
    except:
        return None

def track_location(request):
    file_name = gps_locator()
    if file_name:
        with open(file_name, 'r') as file:
            html_content = file.read()
        return HttpResponse(html_content)
    else:
        return HttpResponse("Error retrieving location data.")

def display_location(request):
    file_name = gps_locator()
    if file_name:
        with open(file_name, 'r') as file:
            html_content = file.read()
        return HttpResponse(html_content)
    else:
        return HttpResponse("Error retrieving location data.")

# Placeholder implementations for location_detail and location_data
def location_detail(request, pk):
    # This is a placeholder. Implement the logic to display location details.
    return HttpResponse(f"Location details for ID {pk}.")

def location_data(request, pk):
    # This is a placeholder. Implement the logic to display real-time location data.
    return HttpResponse(f"Real-time location data for ID {pk}.")
