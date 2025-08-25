# UV Index Command Implementation Prompt

## Overview
Add a new command to the weather CLI application that displays the current UV index for a given zip code.

## Requirements

### Command Specification
- **Command**: `uv` or `uvindex`
- **Usage**: `weather uv <zipcode>` or `weather uvindex <zipcode>`
- **Description**: Display the current UV index and safety recommendations for the specified zip code

### Input Validation
- Validate that the zip code is provided
- Validate zip code format (5 digits for US zip codes)
- Handle invalid zip codes gracefully with appropriate error messages

### Output Format
The command should display:
1. Location (city, state from zip code)
2. Current UV Index value (0-11+ scale)
3. UV Index category (Low, Moderate, High, Very High, Extreme)
4. Safety recommendations based on UV level
5. Timestamp of when the data was retrieved

### Example Output
```
UV Index for 90210 (Beverly Hills, CA):

Current UV Index: 8 (Very High)
Recommendation: Minimize sun exposure between 10 AM and 4 PM. 
Seek shade, wear protective clothing, sunglasses, and use 
SPF 30+ sunscreen.

Data retrieved: August 25, 2025 at 2:30 PM PST
```

### UV Index Scale Reference
- **0-2**: Low (Green) - Minimal risk
- **3-5**: Moderate (Yellow) - Moderate risk  
- **6-7**: High (Orange) - High risk
- **8-10**: Very High (Red) - Very high risk
- **11+**: Extreme (Violet) - Extreme risk

### API Requirements
- Use a free API that doesn't require registration
- Suggested APIs:
  - OpenWeatherMap One Call API (free tier)
  - WeatherAPI.com (free tier)
  - UV Index API from EPA or similar government source

### Error Handling
- Handle network connectivity issues
- Handle API rate limiting
- Handle invalid zip codes
- Handle API service unavailability
- Provide meaningful error messages to users

### Implementation Notes
- Follow the existing CLI app structure and patterns
- Add appropriate help text for the new command
- Include the new command in the main help output
- Ensure consistent styling with existing commands
- Add any new dependencies to requirements.txt

### Testing Considerations
- Test with valid US zip codes
- Test with invalid zip codes
- Test with network connectivity issues
- Test API error responses
- Verify output formatting and readability

### Documentation Updates
- Update README.md with the new command
- Add usage examples
- Document any new configuration options
- Update command reference section
