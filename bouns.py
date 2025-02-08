def input_weather_data(weather_data):
    city = input("enter city name: ")

    if city not in weather_data:
        weather_data[city] = {}

    date = input(f"enter the date for {city} :")
    temperature = float(input(f"enter the temperature for {city} on {date}: "))
    humidity = float(input(f"Enter the humidity for {city} on {date} (in %): "))
    condition = input(f"Enter the weather condition for {city} on {date}: ")

    weather_data[city][date] = {
        'temperature': temperature,
        'humidity': humidity,
        'condition': condition
    }
    
def querey_city(weather_data):
    city = input("Enter city name to query weather: ")

    if city in weather_data:
        print(f"\nWeather Data for {city}:")
        for date, data in weather_data[city].items():
            print(f"\nDate: {date}")
            print(f"Temperature: {data['temperature']}°C")
            print(f"Humidity: {data['humidity']}%")
            print(f"Condition: {data['condition']}")
    else:
        print(f"Weather data for {city} is not available.")



def update_weather(weather_data):
    city = input("enter city name to update weather: ")

    if city in weather_data:
        date = input(f"Enter the date to update for {city} (YYYY-MM-DD): ")
        
        if date in weather_data[city]:
            temperature = float(input(f"Enter the updated temperature for {city} on {date}: "))
            humidity = float(input(f"Enter the updated humidity for {city} on {date} (in %): "))
            condition = input(f"Enter the updated weather condition for {city} on {date}: ")
            
            # Update the data
            weather_data[city][date] = {
                'temperature': temperature,
                'humidity': humidity,
                'condition': condition
            }
            print(f"Weather data for {city} on {date} has been updated.")
        else:
            print(f"No weather data found for {city} on {date}.")
    else:
        print(f"No weather data found for {city}.")

def delete_weather_data(weather_data):
    city = input("Enter city name to delete weather data: ")
    
    if city in weather_data:
        date = input(f"Enter the date to delete for {city} : ")
        
        if date in weather_data[city]:
            del weather_data[city][date]
            print(f"Weather data for {city} on {date} has been deleted.")
        else:
            print(f"No weather data found for {city} on {date}.")
    else:
        print(f"No weather data found for {city}.")

def delete_weather_data(weather_data):
    city = input("Enter city name to delete weather data: ")
    
    if city in weather_data:
        date = input(f"Enter the date to delete for {city} (YYYY-MM-DD): ")
        
        if date in weather_data[city]:
            del weather_data[city][date]
            print(f"Weather data for {city} on {date} has been deleted.")
        else:
            print(f"No weather data found for {city} on {date}.")
    else:
        print(f"No weather data found for {city}.")

def run():
    weather_data = {}

    while True:
        print("\nMenu:")
        print("1. Input Weather Data")
        print("2. Query Weather Data by City")
        print("3. Update Weather Data")
        print("4. Delete Weather Data")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            input_weather_data(weather_data)
        elif choice == "2":
            querey_city(weather_data)
        elif choice == "3":
            update_weather(weather_data)
        elif choice == "4":
            delete_weather_data(weather_data)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

run()