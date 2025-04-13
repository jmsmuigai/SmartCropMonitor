import requests
from django.shortcuts import render

def home(request):
    weather_data = {}
    if 'city' in request.GET:
        city = request.GET['city']
        api_key = '272673e2a3ef998211ae5c4c86845e3f'  # Replace with your valid API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {"message": "City not found or API error."}
    return render(request, 'monitor/home.html', {'weather': weather_data})