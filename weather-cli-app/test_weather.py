#!/usr/bin/env python3
"""
Test script for the Weather CLI App
"""

import subprocess


def run_command(cmd):
    """Run a command and return the result"""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=30, check=False
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Command timed out"


def test_weather_cli():
    """Test the weather CLI application"""
    print("Testing Weather CLI App...")
    print("=" * 50)

    # Test help command
    print("\n1. Testing help command...")
    success, stdout, stderr = run_command("python3 weather.py --help")
    if success and "Weather CLI" in stdout:
        print("✅ Help command works")
    else:
        print("❌ Help command failed")
        print(f"Error: {stderr}")

    # Test invalid zip code
    print("\n2. Testing invalid zip code...")
    success, stdout, stderr = run_command("python3 weather.py current 1234")
    if "Invalid zip code format" in stdout:
        print("✅ Invalid zip code validation works")
    else:
        print("❌ Invalid zip code validation failed")

    # Test current weather
    print("\n3. Testing current weather command...")
    success, stdout, stderr = run_command("python3 weather.py current 90210")
    if success and "Current Weather" in stdout and "Beverly Hills" in stdout:
        print("✅ Current weather command works")
    else:
        print("❌ Current weather command failed")
        print(f"Error: {stderr}")

    # Test UV index
    print("\n4. Testing UV index command...")
    success, stdout, stderr = run_command("python3 weather.py uv 90210")
    if success and "UV Index" in stdout and "Beverly Hills" in stdout:
        print("✅ UV index command works")
    else:
        print("❌ UV index command failed")
        print(f"Error: {stderr}")

    # Test forecast
    print("\n5. Testing forecast command...")
    success, stdout, stderr = run_command("python3 weather.py forecast 10001")
    if success and "Forecast" in stdout and "New York" in stdout:
        print("✅ Forecast command works")
    else:
        print("❌ Forecast command failed")
        print(f"Error: {stderr}")

    print("\n" + "=" * 50)
    print("Testing complete!")


if __name__ == "__main__":
    test_weather_cli()
