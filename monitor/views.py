import requests
from django.shortcuts import render

def home(request):
    weather_data = {}
    if 'city' in request.GET:
        city = request.GET['city']
        api_key = '4b261f097fbd3034e68af34f3d12cb7f'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {"message": "City not found or API error."}
    return render(request, 'monitor/home.html', {'weather': weather_data})