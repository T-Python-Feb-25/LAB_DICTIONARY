# Dictionary to store weather data
weather_data = {}

# Function to add weather data
def add_weather_data():
    city = input("Enter city name: ").strip().title()
    date = input("Enter date (YYYY-MM-DD): ").strip()
    temperature = input("Enter temperature (°C): ").strip()
    humidity = input("Enter humidity (%): ").strip()
    condition = input("Enter weather condition (e.g., sunny, rainy, cloudy): ").strip().lower()

    # Ensure the city exists in the dictionary
    if city not in weather_data:
        weather_data[city] = {}

    # Add weather data for the given date
    weather_data[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }

    print(f"Weather data saved for {city} on {date}.")

# Function to display weather data for a city
def show_weather_data():
    city = input("Enter the city name to view weather data: ").strip().title()
    
    if city in weather_data:
        print(f"\n🌤 Weather data for {city}:")
        for date, details in weather_data[city].items():
            print(f" {date}: Temp {details['temperature']}°C, Humidity {details['humidity']}%, Condition {details['condition']}")
    else:
        print(" No data available for this city.")

# Function to update weather data
def update_weather_data():
    city = input("Enter city name: ").strip().title()
    date = input("Enter date (YYYY-MM-DD) to update: ").strip()

    if city in weather_data and date in weather_data[city]:
        print("\n🌦 Current weather data:")
        print(f" {date}: Temp {weather_data[city][date]['temperature']}°C, Humidity {weather_data[city][date]['humidity']}%, Condition {weather_data[city][date]['condition']}")

        new_temp = input("Enter new temperature (or press Enter to keep the same): ").strip()
        new_humidity = input("Enter new humidity (or press Enter to keep the same): ").strip()
        new_condition = input("Enter new weather condition (or press Enter to keep the same): ").strip()

        if new_temp:
            weather_data[city][date]["temperature"] = new_temp
        if new_humidity:
            weather_data[city][date]["humidity"] = new_humidity
        if new_condition:
            weather_data[city][date]["condition"] = new_condition.lower()

        print(" Weather data updated successfully.")
    else:
        print(" No data found for this city on the given date.")

# Function to delete weather data
def delete_weather_data():
    city = input("Enter city name: ").strip().title()
    date = input("Enter date (YYYY-MM-DD) to delete: ").strip()

    if city in weather_data and date in weather_data[city]:
        del weather_data[city][date]
        print(f" Weather data for {city} on {date} has been deleted.")

        # Remove the city from the dictionary if no more records exist
        if not weather_data[city]:
            del weather_data[city]
    else:
        print(" No data found for this city on the given date.")

# Main menu function
def main():
    while True:
        print("\n Weather Data Management System:")
        print("1️ Add Weather Data")
        print("2️ View Weather Data")
        print("3️ Update Weather Data")
        print("4️ Delete Weather Data")
        print("5️ Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_weather_data()
        elif choice == "2":
            show_weather_data()
        elif choice == "3":
            update_weather_data()
        elif choice == "4":
            delete_weather_data()
        elif choice == "5":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice, please try again.")

# Run the program
    if  __name__ == "_main_":
     main()