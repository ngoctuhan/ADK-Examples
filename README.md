# Agent Development Toolkit (ADK) Examples

This repository demonstrates how to build intelligent agents using Google's Agent Development Toolkit (ADK). It showcases various agent capabilities including multi-tool integration, weather and time services, and mathematical calculations.

## Features

### Multi-tool Agent
A versatile agent that combines multiple tools to provide comprehensive assistance:

- **Weather Information**: Get real-time weather data for any city using OpenWeatherMap API
  - Current temperature
  - Weather conditions
  - Humidity
  - Wind speed

- **Time Services**: Get current time in different cities
  - Timezone-aware responses
  - Date and time information
  - City-specific time queries

- **Calculator**: Perform various mathematical operations
  - Basic arithmetic (+, -, *, /)
  - Advanced operations (exponents, square roots)
  - Trigonometric functions (sin, cos, tan)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ADK-Examples.git
   cd ADK-Examples
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   export OPENWEATHER_API_KEY='your_api_key_here'
   ```

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`:
  - google-adk
  - requests>=2.31.0

## Project Structure

```
ADK-Examples/
├── multi_tool_agent/
│   ├── agent.py          # Main agent implementation
│   └── tools.py          # Tool definitions
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## Usage

The agent can be used to answer various types of queries:

### Weather Queries
```python
# Example: Get weather for a city
response = agent.query("What's the weather like in Tokyo?")
```

### Time Queries
```python
# Example: Get current time in a city
response = agent.query("What time is it in London?")
```

### Mathematical Calculations
```python
# Example: Perform calculations
response = agent.query("Calculate 2 + 2")
response = agent.query("What is sin(45)?")
```

## Development

This project demonstrates:
- Integration of multiple tools in a single agent
- Real-time API integration (OpenWeatherMap)
- Timezone-aware time calculations
- Mathematical computation capabilities

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Resources

- [Google ADK Documentation](https://developers.google.com/adk)
- [OpenWeatherMap API](https://openweathermap.org/api)

adk web to view and test agents 