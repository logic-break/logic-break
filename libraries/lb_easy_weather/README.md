
# lb_easy_weather
© Copyright logic-break 2026

https://github.com/logic-break/logic-break/tree/main/libraries/lb_easy_weather


> lib made for lazy, by lazy  

installation:

    pip install lb-easy-weather

**NOTE: in code, you must import lb_easy_weather**


# Usage:
.get("Minsk") : returns dict, example: {'City': 'Minsk', 'Country': 'Belarus', 'Temp': '6.0°C', 'Wind': '10.8 km/h'}
# Example:
```
import lb_easy_weather as weather

# Get dictionary
data = weather.get("Minsk")
print(data) 
# Output: {'City': 'Minsk', 'Country': 'Belarus', 'Temp': '6.0°C', 'Wind': '10.8 km/h'}
```
