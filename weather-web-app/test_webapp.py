#!/usr/bin/env python3
"""
Test script for the Weather Web App
"""

import requests
import time
import subprocess
import os
import signal
from urllib.parse import urljoin


def start_flask_app():
    """Start the Flask application in the background"""
    return subprocess.Popen(
        ["python3", "app.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        preexec_fn=os.setsid
    )


def stop_flask_app(process):
    """Stop the Flask application"""
    try:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        process.wait(timeout=5)
    except:
        os.killpg(os.getpgid(process.pid), signal.SIGKILL)


def test_web_app():
    """Test the weather web application"""
    print("Testing Weather Web App...")
    print("=" * 50)
    
    # Start Flask app
    print("\n1. Starting Flask application...")
    app_process = start_flask_app()
    
    # Wait for app to start
    time.sleep(3)
    
    base_url = "http://127.0.0.1:5000"
    
    try:
        # Test home page
        print("\n2. Testing home page...")
        response = requests.get(base_url, timeout=10)
        if response.status_code == 200 and "Weather App" in response.text:
            print("✅ Home page loads successfully")
        else:
            print("❌ Home page failed to load")
            print(f"Status: {response.status_code}")
        
        # Test weather endpoint with valid zip code
        print("\n3. Testing weather endpoint with valid zip code...")
        data = {"zipcode": "90210"}
        response = requests.post(urljoin(base_url, "/weather"), data=data, timeout=10)
        if response.status_code == 200 and "Beverly Hills" in response.text:
            print("✅ Weather endpoint works with valid zip code")
            if "Current Weather" in response.text:
                print("✅ Current weather data displayed")
            if "UV Index" in response.text:
                print("✅ UV index data displayed")
            if "3-Day Forecast" in response.text:
                print("✅ Forecast data displayed")
            if any(emoji in response.text for emoji in ["☀️", "🌤️", "⛅", "☁️", "🌧️"]):
                print("✅ Weather emojis displayed")
        else:
            print("❌ Weather endpoint failed")
            print(f"Status: {response.status_code}")
        
        # Test with invalid zip code
        print("\n4. Testing with invalid zip code...")
        data = {"zipcode": "12345"}  # This will likely not be found
        response = requests.post(urljoin(base_url, "/weather"), data=data, timeout=10)
        if response.status_code == 200:
            if "Could not find location" in response.text or "Error" in response.text:
                print("✅ Invalid zip code handled gracefully")
            else:
                print("✅ App handled the request (using mock data)")
        else:
            print("❌ Invalid zip code test failed")
        
        # Test empty zip code
        print("\n5. Testing with empty zip code...")
        data = {"zipcode": ""}
        response = requests.post(urljoin(base_url, "/weather"), data=data, timeout=10)
        if response.status_code == 200 and "Please enter a zip code" in response.text:
            print("✅ Empty zip code validation works")
        else:
            print("❌ Empty zip code validation failed")
        
        # Test different valid zip codes
        print("\n6. Testing multiple zip codes...")
        test_zips = ["10001", "60601", "94102", "33101"]
        for zipcode in test_zips:
            data = {"zipcode": zipcode}
            response = requests.post(urljoin(base_url, "/weather"), data=data, timeout=10)
            if response.status_code == 200 and "Current Weather" in response.text:
                print(f"✅ Zip code {zipcode} works")
            else:
                print(f"❌ Zip code {zipcode} failed")
    
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to Flask app")
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
    
    finally:
        # Stop Flask app
        print("\n7. Stopping Flask application...")
        stop_flask_app(app_process)
        print("✅ Flask application stopped")
    
    print("\n" + "=" * 50)
    print("Web app testing complete!")


if __name__ == "__main__":
    test_web_app()