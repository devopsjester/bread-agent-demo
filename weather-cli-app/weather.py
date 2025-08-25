#!/usr/bin/env python3
"""
Weather CLI App
A command-line tool for getting weather information by zip code.
"""

import click
import requests
import json
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init(autoreset=True)


class WeatherAPI:
    """Weather API client using OpenWeatherMap's free tier"""

    def __init__(self):
        # Using OpenWeatherMap's free API (no key required for basic usage)
        self.base_url = "http://api.openweathermap.org/data/2.5"
        # For demo purposes, using a public endpoint that doesn't require API key
        # In production, you'd want to use a proper API key

    def get_coordinates(self, zipcode):
        """Get latitude and longitude from zip code using a free geocoding service"""
        try:
            # Using a free geocoding service
            url = f"http://api.zippopotam.us/us/{zipcode}"
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                lat = float(data["places"][0]["latitude"])
                lon = float(data["places"][0]["longitude"])
                city = data["places"][0]["place name"]
                state = data["places"][0]["state abbreviation"]
                return lat, lon, f"{city}, {state}"
            else:
                return None, None, None
        except Exception as e:
            return None, None, None

    def get_weather_data(self, lat, lon):
        """Get weather data using a free weather API"""
        try:
            # Using Open-Meteo API (free, no registration required)
            url = f"https://api.open-meteo.com/v1/forecast"
            params = {
                "latitude": lat,
                "longitude": lon,
                "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
                "daily": "temperature_2m_max,temperature_2m_min,weather_code",
                "temperature_unit": "fahrenheit",
                "wind_speed_unit": "mph",
                "timezone": "auto",
                "forecast_days": 3,
            }

            response = requests.get(url, params=params, timeout=10)

            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            return None

    def get_uv_index(self, lat, lon):
        """Get UV index data using a free API"""
        try:
            # Using Open-Meteo API for UV index
            url = f"https://api.open-meteo.com/v1/forecast"
            params = {
                "latitude": lat,
                "longitude": lon,
                "current": "uv_index",
                "timezone": "auto",
            }

            response = requests.get(url, params=params, timeout=10)

            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            return None


def get_weather_description(weather_code):
    """Convert weather code to description"""
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail",
    }
    return weather_codes.get(weather_code, "Unknown")


def get_uv_category(uv_index):
    """Get UV index category and color"""
    if uv_index <= 2:
        return "Low", Fore.GREEN
    elif uv_index <= 5:
        return "Moderate", Fore.YELLOW
    elif uv_index <= 7:
        return "High", Fore.MAGENTA
    elif uv_index <= 10:
        return "Very High", Fore.RED
    else:
        return "Extreme", Fore.MAGENTA


def get_uv_recommendation(uv_index):
    """Get UV safety recommendation"""
    if uv_index <= 2:
        return "Minimal risk. Wear sunglasses on bright days."
    elif uv_index <= 5:
        return "Moderate risk. Seek shade during midday hours. Wear sunglasses and sunscreen."
    elif uv_index <= 7:
        return "High risk. Reduce time in the sun between 10 AM and 4 PM. Wear protective clothing, sunglasses, and sunscreen."
    elif uv_index <= 10:
        return "Very high risk. Minimize sun exposure between 10 AM and 4 PM. Seek shade, wear protective clothing, sunglasses, and use SPF 30+ sunscreen."
    else:
        return "Extreme risk. Avoid sun exposure between 10 AM and 4 PM. Stay in shade, wear protective clothing, and use SPF 30+ sunscreen."


def validate_zipcode(zipcode):
    """Validate US zip code format"""
    if len(zipcode) != 5 or not zipcode.isdigit():
        return False
    return True


@click.group()
def cli():
    """Weather CLI - Get weather information by zip code"""
    pass


@cli.command()
@click.argument("zipcode")
def current(zipcode):
    """Get current weather for a zip code"""
    if not validate_zipcode(zipcode):
        click.echo(
            f"{Fore.RED}Error: Invalid zip code format. Please enter a 5-digit US zip code.{Style.RESET_ALL}"
        )
        return

    api = WeatherAPI()

    # Get coordinates from zip code
    click.echo(f"Getting weather for zip code {zipcode}...")
    lat, lon, location = api.get_coordinates(zipcode)

    if lat is None:
        click.echo(
            f"{Fore.RED}Error: Could not find location for zip code {zipcode}{Style.RESET_ALL}"
        )
        return

    # Get weather data
    weather_data = api.get_weather_data(lat, lon)

    if weather_data is None:
        click.echo(f"{Fore.RED}Error: Could not retrieve weather data{Style.RESET_ALL}")
        return

    # Display current weather
    current_data = weather_data["current"]
    temp = current_data["temperature_2m"]
    humidity = current_data["relative_humidity_2m"]
    wind_speed = current_data["wind_speed_10m"]
    weather_code = current_data["weather_code"]
    description = get_weather_description(weather_code)

    click.echo(f"\n{Fore.CYAN}Current Weather for {location}:{Style.RESET_ALL}")
    click.echo(f"Temperature: {Fore.YELLOW}{temp}°F{Style.RESET_ALL}")
    click.echo(f"Conditions: {description}")
    click.echo(f"Humidity: {humidity}%")
    click.echo(f"Wind Speed: {wind_speed} mph")
    click.echo(f"Data retrieved: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}")


@cli.command()
@click.argument("zipcode")
def forecast(zipcode):
    """Get 3-day weather forecast for a zip code"""
    if not validate_zipcode(zipcode):
        click.echo(
            f"{Fore.RED}Error: Invalid zip code format. Please enter a 5-digit US zip code.{Style.RESET_ALL}"
        )
        return

    api = WeatherAPI()

    # Get coordinates from zip code
    click.echo(f"Getting forecast for zip code {zipcode}...")
    lat, lon, location = api.get_coordinates(zipcode)

    if lat is None:
        click.echo(
            f"{Fore.RED}Error: Could not find location for zip code {zipcode}{Style.RESET_ALL}"
        )
        return

    # Get weather data
    weather_data = api.get_weather_data(lat, lon)

    if weather_data is None:
        click.echo(f"{Fore.RED}Error: Could not retrieve weather data{Style.RESET_ALL}")
        return

    # Display forecast
    daily_data = weather_data["daily"]
    dates = daily_data["time"]
    max_temps = daily_data["temperature_2m_max"]
    min_temps = daily_data["temperature_2m_min"]
    weather_codes = daily_data["weather_code"]

    click.echo(f"\n{Fore.CYAN}3-Day Forecast for {location}:{Style.RESET_ALL}")

    for i in range(len(dates)):
        date = datetime.fromisoformat(dates[i]).strftime("%A, %B %d")
        max_temp = max_temps[i]
        min_temp = min_temps[i]
        description = get_weather_description(weather_codes[i])

        click.echo(f"\n{Fore.YELLOW}{date}{Style.RESET_ALL}")
        click.echo(f"  High: {max_temp}°F | Low: {min_temp}°F")
        click.echo(f"  Conditions: {description}")


@cli.command()
@click.argument("zipcode")
def uv(zipcode):
    """Get current UV index for a zip code"""
    if not validate_zipcode(zipcode):
        click.echo(
            f"{Fore.RED}Error: Invalid zip code format. Please enter a 5-digit US zip code.{Style.RESET_ALL}"
        )
        return

    api = WeatherAPI()

    # Get coordinates from zip code
    click.echo(f"Getting UV index for zip code {zipcode}...")
    lat, lon, location = api.get_coordinates(zipcode)

    if lat is None:
        click.echo(
            f"{Fore.RED}Error: Could not find location for zip code {zipcode}{Style.RESET_ALL}"
        )
        return

    # Get UV index data
    uv_data = api.get_uv_index(lat, lon)

    if uv_data is None:
        click.echo(
            f"{Fore.RED}Error: Could not retrieve UV index data{Style.RESET_ALL}"
        )
        return

    # Display UV index
    current_uv = uv_data["current"]["uv_index"]
    category, color = get_uv_category(current_uv)
    recommendation = get_uv_recommendation(current_uv)

    click.echo(f"\n{Fore.CYAN}UV Index for {location}:{Style.RESET_ALL}")
    click.echo(
        f"Current UV Index: {color}{current_uv:.1f} ({category}){Style.RESET_ALL}"
    )
    click.echo(f"Recommendation: {recommendation}")
    click.echo(f"\nData retrieved: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}")


@cli.command()
@click.argument("zipcode")
def uvindex(zipcode):
    """Alias for uv command - Get current UV index for a zip code"""
    # Call the uv command
    uv.callback(zipcode)


if __name__ == "__main__":
    cli()
