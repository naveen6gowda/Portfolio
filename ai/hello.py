import requests

# We need coordinates to get weather data
latitude = 48.14   # Munich latitude
longitude = 11.58  # Munich longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)

Temp = data["current"]["temperature_2m"]

print(f"Current Temperature at Munich is : {Temp}°C")