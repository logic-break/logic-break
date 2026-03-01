import urllib.request
import json

def get(city):
	"""Returns weather data as a dictionary: {'City', 'Country', 'Temp', 'Wind'}"""
	try:
		geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
		with urllib.request.urlopen(geo_url) as resp:
			geo_data = json.loads(resp.read().decode())
		
		if not geo_data.get('results'):
			return f"Error: City '{city}' not found."
		
		loc = geo_data['results'][0]

		weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={loc['latitude']}&longitude={loc['longitude']}&current_weather=true"
		with urllib.request.urlopen(weather_url) as resp:
			data = json.loads(resp.read().decode())
			
		curr = data['current_weather']
		
		return {
			'City': loc['name'],
			'Country': loc.get('country', 'N/A'),
			'Temp': f"{curr['temperature']}°C",
			'Wind': f"{curr['windspeed']} km/h"
		}
	except Exception as e:
		return f"Error: {e}"
