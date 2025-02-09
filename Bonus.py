
weather_data = {}


def add_weather_data():
    city = input("Enter city name: ").capitalize()
    date = input("Enter date (YYYY-MM-DD): ")
    temperature = input("Enter temperature (°C): ")
    humidity = input("Enter humidity (%): ")
    condition = input("Enter weather condition (e.g., sunny, rainy): ").capitalize()
    
    if city not in weather_data:
        weather_data[city] = {}
    
    weather_data[city][date] = {
        "Temperature": f"{temperature}°C",
        "Humidity": f"{humidity}%",
        "Condition": condition
    }
    print(f"Weather data added for {city} on {date}.")


def query_weather():
    city = input("Enter city name to query: ").capitalize()
    if city in weather_data:
        print(f"Weather data for {city}:")
        for date, details in weather_data[city].items():
            print(f"{date} - Temperature: {details['Temperature']}, Humidity: {details['Humidity']}, Condition: {details['Condition']}")
    else:
        print("No weather data found for this city.")


def update_weather():
    city = input("Enter city name to update: ").capitalize()
    date = input("Enter date to update (YYYY-MM-DD): ")
    
    if city in weather_data and date in weather_data[city]:
        print("Enter new values (press Enter to keep existing value):")
        temperature = input(f"New Temperature ({weather_data[city][date]['Temperature']}): ") or weather_data[city][date]['Temperature']
        humidity = input(f"New Humidity ({weather_data[city][date]['Humidity']}): ") or weather_data[city][date]['Humidity']
        condition = input(f"New Condition ({weather_data[city][date]['Condition']}): ").capitalize() or weather_data[city][date]['Condition']
        
        weather_data[city][date] = {
            "Temperature": temperature,
            "Humidity": humidity,
            "Condition": condition
        }
        print(f"Weather data for {city} on {date} updated.")
    else:
        print("Weather data not found for this city and date.")


def delete_weather():
    city = input("Enter city name to delete data from: ").capitalize()
    date = input("Enter date to delete (YYYY-MM-DD): ")
    
    if city in weather_data and date in weather_data[city]:
        del weather_data[city][date]
        if not weather_data[city]:  
            del weather_data[city]
        print(f"Weather data for {city} on {date} deleted.")
    else:
        print("Weather data not found for this city and date.")


while True:
    print("\nWeather Data Menu:")
    print("1. Add Weather Data")
    print("2. Query Weather Data")
    print("3. Update Weather Data")
    print("4. Delete Weather Data")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_weather_data()
    elif choice == "2":
        query_weather()
    elif choice == "3":
        update_weather()
    elif choice == "4":
        delete_weather()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
