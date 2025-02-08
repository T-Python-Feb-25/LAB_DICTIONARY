def add_weather_data(data):
    city_name = input("Enter city name: ").strip()
    record_date = input("Enter date (YYYY-MM-DD): ").strip()
    temp = input("Enter temperature (°C): ").strip()
    hum = input("Enter humidity (%): ").strip()
    weather_cond = input("Enter weather condition (e.g., sunny, rainy): ").strip()

    if city_name not in data:
        data[city_name] = {}
    data[city_name][record_date] = {
        "temperature": temp,
        "humidity": hum,
        "condition": weather_cond
    }
    print(f"Weather data for {city_name} on {record_date} has been added.")

def view_weather_data(data):
    city_name = input("Enter city name to query: ").strip()
    if city_name in data:
        print(f"Weather data for {city_name}:")
        for record_date, details in data[city_name].items():
            print(f"  Date: {record_date}, Temperature: {details['temperature']}°C, "
                  f"Humidity: {details['humidity']}%, Condition: {details['condition']}")
    else:
        print(f"No weather data found for {city_name}.")

def edit_weather_data(data):
    city_name = input("Enter city name to update: ").strip()
    if city_name in data:
        record_date = input("Enter date to update (YYYY-MM-DD): ").strip()
        if record_date in data[city_name]:
            temp = input("Enter new temperature (°C): ").strip()
            hum = input("Enter new humidity (%): ").strip()
            weather_cond = input("Enter new weather condition: ").strip()
            data[city_name][record_date] = {
                "temperature": temp,
                "humidity": hum,
                "condition": weather_cond
            }
            print(f"Weather data for {city_name} on {record_date} has been updated.")
        else:
            print(f"No weather data found for {city_name} on {record_date}.")
    else:
        print(f"No weather data found for {city_name}.")

def remove_weather_data(data):
    city_name = input("Enter city name to delete data from: ").strip()
    if city_name in data:
        record_date = input("Enter date to delete data (YYYY-MM-DD): ").strip()
        if record_date in data[city_name]:
            del data[city_name][record_date]
            print(f"Weather data for {city_name} on {record_date} has been deleted.")
            if not data[city_name]:
                del data[city_name]
        else:
            print(f"No weather data found for {city_name} on {record_date}.")
    else:
        print(f"No weather data found for {city_name}.")

def main():
    records = {}
    while True:
        print("\nMenu:")
        print("1. Add weather data")
        print("2. View weather data by city")
        print("3. Edit weather data")
        print("4. Remove weather data")
        print("5. Exit")
        option = input("Enter your choice: ").strip()

        if option == "1":
            add_weather_data(records)
        elif option == "2":
            view_weather_data(records)
        elif option == "3":
            edit_weather_data(records)
        elif option == "4":
            remove_weather_data(records)
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
