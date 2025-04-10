import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from multi_tool_agent.tools import get_weather, get_current_time, calculator
from google.adk.tools import google_search 
root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the time, weather, and perform calculations."
    ),
    instruction=(
        "You are a helpful assistant. You can answer your questions about the time and weather or temperature in a city, "
        "and perform mathematical calculations."
    ),
    tools=[get_weather, get_current_time, calculator],
)