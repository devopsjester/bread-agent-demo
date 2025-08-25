# Weather Apps Demo

This repository contains both a command-line interface (CLI) and web application for getting weather information by US zip code.

## 🌤️ Web Application

A modern, responsive web app with an intuitive interface for weather information.

**Features:**
- Real-time current weather conditions
- 3-day weather forecast
- UV index with safety recommendations  
- Weather emojis for visual representation
- Responsive design for mobile and desktop

**Location:** `weather-web-app/`

![Weather Web App](https://github.com/user-attachments/assets/813da81e-b91b-459d-8c7d-5193be5e3dbc)

## 💻 CLI Application

A command-line tool for weather information with colorized output.

**Features:**
- Current weather by zip code
- 3-day forecast
- UV index with recommendations
- Colorized terminal output

**Location:** `weather-cli-app/`

## 🚀 Quick Start

### Web App
```bash
cd weather-web-app
python3 -m pip install -r requirements.txt
python3 app.py
# Open http://127.0.0.1:5000 in your browser
```

### CLI App  
```bash
cd weather-cli-app
python3 -m pip install -r requirements.txt
python3 weather.py current 90210
```

## 🌐 APIs Used

Both applications use free APIs that don't require registration:
- **Zippopotam.us**: ZIP code to coordinates conversion
- **Open-Meteo**: Weather data and UV index information

## 📱 Screenshots

### Web App Home
![Home Page](https://github.com/user-attachments/assets/293a41f6-0570-42cc-8ec7-3bf288ecad0e)

### Web App Results  
![Weather Results](https://github.com/user-attachments/assets/813da81e-b91b-459d-8c7d-5193be5e3dbc)
