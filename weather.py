
import requests

def get_weather(city, api_key):
    try:
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric",  # For Celsius, use "imperial" for Fahrenheit
        }
        
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error: {response.status_code} - {response.reason}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def display_weather(data):
    if data:
        city = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print("\nWeather Information:")
        print(f"City: {city}, {country}")
        print(f"Temperature: {temperature}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Weather: {weather.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Unable to fetch weather data.")

def main():
    print("Welcome to the Weather App!")
    
    api_key = "your_api_key_here"

    while True:
        city = input("\nEnter the name of the city (or type 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Goodbye!")
            break

        weather_data = get_weather(city, api_key)
        display_weather(weather_data)

if __name__ == "__main__":
    main()
