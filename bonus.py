from datetime import datetime

# Function to check if city name is valid
def is_valid_city_name(city_name):
    return city_name.isalpha() and len(city_name) > 0

# Function to check if the date is valid (adjusted format to dd/mm/yyyy)
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%d/%m/%Y")  # Convert the string to date (dd/mm/yyyy format)
        return True
    except ValueError:
        return False  # If it doesn't match the format, return False

# Function to check if temperature is a valid number
def is_valid_temperature(temp):
    try:
        float(temp)  # Try to convert to a float
        return True
    except ValueError:
        return False  # If it can't be converted, return False

# Function to check if humidity is a number between 0 and 100
def is_valid_humidity(humidity):
    try:
        hum = int(humidity)
        return 0 <= hum <= 100  # Check if humidity is in the valid range (0 to 100)
    except ValueError:
        return False

# Function to get weather data
def get_weather_data():
    weather_info = {}
    
    while True:
        city_name = input("Enter the city name (or 'done' to finish): ")
        if city_name.lower() == 'done':
            break

        if not is_valid_city_name(city_name):
            print("Invalid city name! Please enter a valid city.")
            continue
        
        date = input("Enter the date (dd/mm/yyyy): ")
        if not is_valid_date(date):
            print("Invalid date format! Please enter the date in dd/mm/yyyy format.")
            continue
        
        temperature = input("Enter the temperature: ")
        if not is_valid_temperature(temperature):
            print("Invalid temperature! Please enter a valid number.")
            continue
        
        humidity = input("Enter the humidity: ")
        if not is_valid_humidity(humidity):
            print("Invalid humidity! Please enter a valid number between 0 and 100.")
            continue
        
        weather_condition = input("Enter the weather condition: ")
        
        # Store the data for each city in the dictionary
        if city_name not in weather_info:
            weather_info[city_name] = {}

        # Add the weather data for the specific date
        weather_info[city_name][date] = {
            'temperature': temperature,
            'humidity': humidity,
            'weather_condition': weather_condition
        }
    
    return weather_info

# Function to query weather information by city
def query_city_weather(weather_info):
    while True:
        city_query = input("Enter a city name to query the weather (or type 'done' to stop): ")
        
        if city_query.lower() == 'done':
            break
        
        # Check if the city exists in the weather data
        if city_query in weather_info:
            print(f"\nWeather Information for {city_query}:")
            for date, data in weather_info[city_query].items():
                print(f"  Date: {date}")
                print(f"    Temperature: {data['temperature']}°C")
                print(f"    Humidity: {data['humidity']}%")
                print(f"    Condition: {data['weather_condition']}\n")
        else:
            print(f"'{city_query}' not found in the weather data.\n")

# Function to update weather information for a specific city and date
def update_weather_data(weather_info):
    city_name = input("Enter the city name to update: ")
    if city_name in weather_info:
        date = input("Enter the date (dd/mm/yyyy) of the data to update: ")
        if date in weather_info[city_name]:
            print("Current data:", weather_info[city_name][date])
            
            # Allow user to update data
            temperature = input("Enter the new temperature: ")
            humidity = input("Enter the new humidity: ")
            weather_condition = input("Enter the new weather condition: ")

            # Update the data
            weather_info[city_name][date] = {
                'temperature': temperature,
                'humidity': humidity,
                'weather_condition': weather_condition
            }
            print(f"Weather data for {city_name} on {date} updated successfully.\n")
        else:
            print(f"No weather data found for {city_name} on {date}.\n")
    else:
        print(f"City {city_name} not found.\n")

# Function to delete weather information for a specific city and date
def delete_weather_data(weather_info):
    city_name = input("Enter the city name to delete data: ")
    if city_name in weather_info:
        date = input("Enter the date (dd/mm/yyyy) of the data to delete: ")
        if date in weather_info[city_name]:
            del weather_info[city_name][date]
            print(f"Weather data for {city_name} on {date} deleted successfully.\n")
        else:
            print(f"No weather data found for {city_name} on {date}.\n")
    else:
        print(f"City {city_name} not found.\n")

# Main Program
def main():
    weather_info = get_weather_data()  # Collect weather data from the user
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Query weather data by city")
        print("2. Update weather data")
        print("3. Delete weather data")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            query_city_weather(weather_info)
        elif choice == '2':
            update_weather_data(weather_info)
        elif choice == '3':
            delete_weather_data(weather_info)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
