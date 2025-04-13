import requests
from django.shortcuts import render

def home(request):
    weather_data = {}
    if 'city' in request.GET:
        city = request.GET['city']
        api_key = 'your_openweather_api_key'  # 🔁 Replace with real API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {"message": "City not found or API error."}
    return render(request, 'monitor/home.html', {'weather': weather_data})