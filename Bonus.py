weather = {
    "Abha": {
        "temperature": 18,
        "humidity": 16,
        "condition": " sunny "
    },
    "Riyadh": {
        "temperature": 30,
        "humidity": 20,
        "condition": " cloudy "
    },
    "Jeddah": {
        "temperature": 28,
        "humidity": 50,
        "condition": " sunny "
    }
}

city = input("Enter the city name to query the weather data: ")

if city in weather:
    print(f"Weather data for {city}:")
    print(f"  Temperature: {weather[city]['temperature']} °C")
    print(f"  Humidity: {weather[city]['humidity']}%")
    print(f"  Condition: {weather[city]['condition']}")
else:
    print("City not found.")