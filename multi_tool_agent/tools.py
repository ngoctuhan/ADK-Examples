import datetime
from zoneinfo import ZoneInfo
import math
import operator
import requests
import os
from typing import Dict, Optional

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city using OpenWeatherMap API.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    # Get API key from environment variable
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        return {
            "status": "error",
            "error_message": "OpenWeatherMap API key not found. Please set OPENWEATHER_API_KEY environment variable."
        }

    # Base URL for OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    try:
        # Make API request
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'  # Use metric units (Celsius)
        }
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise exception for bad status codes
        
        data = response.json()
        
        # Extract relevant weather information
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        report = (
            f"The weather in {city} is {description} with a temperature of {temperature}°C. "
            f"Humidity is {humidity}% and wind speed is {wind_speed} m/s."
        )
        
        return {
            "status": "success",
            "report": report
        }
        
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "error_message": f"Error fetching weather data: {str(e)}"
        }
    except (KeyError, IndexError) as e:
        return {
            "status": "error",
            "error_message": f"Error processing weather data: {str(e)}"
        }


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}

def calculator(expression: str) -> dict:
    """Evaluates a mathematical expression.

    Args:
        expression (str): The mathematical expression to evaluate.
                         Supports basic operations: +, -, *, /, **, sqrt, sin, cos, tan.

    Returns:
        dict: status and result or error msg.
    """
    try:
        # Define safe operations
        safe_ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '**': operator.pow,
            'sqrt': math.sqrt,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
        }
        
        # Clean and prepare expression
        expression = expression.replace('sqrt', 'safe_ops["sqrt"]')
        expression = expression.replace('sin', 'safe_ops["sin"]')
        expression = expression.replace('cos', 'safe_ops["cos"]')
        expression = expression.replace('tan', 'safe_ops["tan"]')
        
        # Evaluate the expression in a safe context
        result = eval(expression, {"__builtins__": {}}, {"safe_ops": safe_ops})
        
        return {
            "status": "success",
            "report": f"The result of '{expression}' is {result}"
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error in calculation: {str(e)}"
        }


