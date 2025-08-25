# Weather Web App

A modern web application that provides weather information for any US zip code, built with Flask and featuring an intuitive user interface.

## Features

- **🌡️ Current Weather**: Real-time temperature, humidity, wind speed, and conditions
- **📅 3-Day Forecast**: Upcoming weather with high/low temperatures 
- **☀️ UV Index**: Current UV levels with safety recommendations and color-coded categories
- **🎨 Weather Emojis**: Visual weather representation for better user experience
- **📱 Responsive Design**: Works beautifully on desktop and mobile devices
- **🔍 Input Validation**: Ensures valid 5-digit US zip codes
- **🆓 Free APIs**: Uses free weather services that don't require registration

## Screenshots

### Home Page
![Weather Web App Home](https://github.com/user-attachments/assets/293a41f6-0570-42cc-8ec7-3bf288ecad0e)

### Weather Results
![Weather Web App Results](https://github.com/user-attachments/assets/813da81e-b91b-459d-8c7d-5193be5e3dbc)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd weather-web-app
   ```

2. **Install dependencies**:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python3 app.py
   ```

4. **Open in browser**:
   Navigate to `http://127.0.0.1:5000` in your web browser

## Usage

1. **Enter a ZIP Code**: Type a 5-digit US ZIP code in the input field
2. **Get Weather**: Click the "Get Weather" button to retrieve weather information
3. **View Results**: See current weather, UV index, and 3-day forecast with weather emojis
4. **Try Examples**: Use the provided example ZIP codes for quick testing

### Example ZIP Codes

- `90210` - Beverly Hills, CA
- `10001` - New York, NY  
- `60601` - Chicago, IL
- `94102` - San Francisco, CA
- `33101` - Miami, FL

## Technical Details

### Architecture

The web app reuses the core weather logic from the CLI app with these components:

- **Flask Web Framework**: Handles HTTP requests and routing
- **WeatherAPI Class**: Manages API calls to weather services
- **Jinja2 Templates**: Renders dynamic HTML with weather data
- **Bootstrap CSS**: Provides responsive styling and components
- **Custom CSS**: Adds weather-themed styling and animations

### APIs Used

- **Zippopotam.us**: Free geocoding service for ZIP code to coordinates conversion
- **Open-Meteo**: Free weather data and UV index information
- **Mock Data**: Fallback data for demonstration when APIs are unavailable

### File Structure

```
weather-web-app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html        # Home page template
│   └── weather.html      # Weather results template
├── static/
│   └── style.css         # Custom CSS styling
└── README.md             # This file
```

## Weather Emojis

The app uses intuitive weather emojis to represent conditions:

- ☀️ Clear sky
- 🌤️ Mainly clear  
- ⛅ Partly cloudy
- ☁️ Overcast
- 🌫️ Fog
- 🌦️ Light rain/drizzle
- 🌧️ Rain
- ⛈️ Thunderstorm/Heavy rain
- 🌨️ Light snow
- ❄️ Heavy snow

## UV Index Scale

The app displays UV index with color-coded categories:

- **0-2**: Low (Green) - Minimal risk
- **3-5**: Moderate (Yellow) - Moderate risk
- **6-7**: High (Orange) - High risk  
- **8-10**: Very High (Red) - Very high risk
- **11+**: Extreme (Purple) - Extreme risk

## Error Handling

The application gracefully handles various error scenarios:

- Invalid ZIP code formats (client-side validation)
- Unknown ZIP codes
- Network connectivity issues
- API service unavailability
- Missing or malformed API responses

## Development

### Running in Development Mode

The Flask app runs in debug mode by default, enabling:
- Automatic reloading on code changes
- Detailed error messages
- Debug toolbar (if installed)

### Production Deployment

For production deployment:

1. Set `debug=False` in `app.py`
2. Use a production WSGI server like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn app:app
   ```
3. Configure a reverse proxy (nginx/Apache) if needed
4. Set up proper logging and monitoring

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.