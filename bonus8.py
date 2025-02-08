# Weather Data Aggregation Program

def add_weather_data(weather_db):
    """Add weather data for a specific city"""
    city = input("Enter city name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    temperature = input("Enter temperature (°C): ")
    humidity = input("Enter humidity (%): ")
    condition = input("Enter weather condition (sunny, rainy, etc.): ")
    
    if city not in weather_db:
        weather_db[city] = {}
    
    weather_db[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }
    print("Weather data added successfully!\n")

def query_weather_data(weather_db):
    """Display weather data for a specific city"""
    city = input("Enter city name to query: ")
    if city in weather_db:
        print(f"Weather data for {city}:")
        for date, data in weather_db[city].items():
            print(f"Date: {date}, Temp: {data['temperature']}°C, Humidity: {data['humidity']}%, Condition: {data['condition']}")
    else:
        print("No data found for this city.\n")

def update_weather_data(weather_db):
    """Update weather data for a specific city and date"""
    city = input("Enter city name: ")
    date = input("Enter date (YYYY-MM-DD) to update: ")
    
    if city in weather_db and date in weather_db[city]:
        temperature = input("Enter new temperature (°C): ")
        humidity = input("Enter new humidity (%): ")
        condition = input("Enter new weather condition: ")
        
        weather_db[city][date] = {
            "temperature": temperature,
            "humidity": humidity,
            "condition": condition
        }
        print("Weather data updated successfully!\n")
    else:
        print("No data found for this city and date.\n")

def delete_weather_data(weather_db):
    """Delete weather data for a specific city and date"""
    city = input("Enter city name: ")
    date = input("Enter date (YYYY-MM-DD) to delete: ")
    
    if city in weather_db and date in weather_db[city]:
        del weather_db[city][date]
        print("Weather data deleted successfully!\n")
    else:
        print("No data found for this city and date.\n")

# Dictionary to store weather data
weather_db = {}

while True:
    print("\nWeather Data Aggregation System")
    print("1. Add Weather Data")
    print("2. Query Weather Data")
    print("3. Update Weather Data")
    print("4. Delete Weather Data")
    print("5. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_weather_data(weather_db)
    elif choice == "2":
        query_weather_data(weather_db)
    elif choice == "3":
        update_weather_data(weather_db)
    elif choice == "4":
        delete_weather_data(weather_db)
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.\n")
