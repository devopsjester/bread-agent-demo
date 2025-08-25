# Weather CLI App

A command-line weather application that provides current weather, forecasts, and UV index information for any US zip code.

## Features

- **Current Weather**: Get real-time weather conditions
- **3-Day Forecast**: View upcoming weather with high/low temperatures
- **UV Index**: Check current UV levels with safety recommendations
- **Colorized Output**: Easy-to-read colored terminal output
- **Free APIs**: Uses free services that don't require registration

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

## Usage

Make the script executable (optional):
```bash
chmod +x weather.py
```

### Available Commands

#### Current Weather
```bash
python3 weather.py current <zipcode>
```
Example:
```bash
python3 weather.py current 90210
```

#### 3-Day Forecast
```bash
python3 weather.py forecast <zipcode>
```
Example:
```bash
python3 weather.py forecast 10001
```

#### UV Index
```bash
python3 weather.py uv <zipcode>
# or
python3 weather.py uvindex <zipcode>
```
Example:
```bash
python3 weather.py uv 33101
```

#### Help
```bash
python3 weather.py --help
python3 weather.py <command> --help
```

### Example Output

**Current Weather:**
```
Current Weather for Beverly Hills, CA:
Temperature: 75°F
Conditions: Partly cloudy
Humidity: 65%
Wind Speed: 8 mph
Data retrieved: August 25, 2025 at 2:30 PM
```

**UV Index:**
```
UV Index for Beverly Hills, CA:
Current UV Index: 8.0 (Very High)
Recommendation: Very high risk. Minimize sun exposure between 10 AM and 4 PM. 
Seek shade, wear protective clothing, sunglasses, and use SPF 30+ sunscreen.

Data retrieved: August 25, 2025 at 2:30 PM
```

## UV Index Scale

- **0-2**: Low (Green) - Minimal risk
- **3-5**: Moderate (Yellow) - Moderate risk  
- **6-7**: High (Orange) - High risk
- **8-10**: Very High (Red) - Very high risk
- **11+**: Extreme (Violet) - Extreme risk

## APIs Used

This application uses free APIs that don't require registration:

- **Zippopotam.us**: For zip code to coordinates conversion
- **Open-Meteo**: For weather data and UV index information

## Error Handling

The application handles various error scenarios:
- Invalid zip code formats
- Network connectivity issues
- API service unavailability
- Invalid or unknown zip codes

## Dependencies

- `requests`: HTTP library for API calls
- `click`: Command-line interface framework
- `colorama`: Cross-platform colored terminal output

## License

This project is open source and available under the MIT License.
