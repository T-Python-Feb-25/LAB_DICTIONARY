def get_weather_data(): # task 1: Input Weather Data
    weather_info = { }
    while True :
        city_name= input("Enter the city name:(or 'done' to finish)  ")
        if city_name.lower() == 'done':
            break
        date = input("Enter the date:(dd/mm/year) ")
        temperature = input("Enter the temperature: ") 
        humidity = input("Enter the humidity: ")
        weather_condition = input("Enter the weather condition: ")
        weather_info[city_name] = (date, temperature, humidity, weather_condition)
         
        # Create a nested dictionary for each city
        weather_info[city_name] = {
            'date': date,
            'temperature': temperature,
            'humidity': humidity,
            'weather_condition': weather_condition
        }
    return weather_info

def query_city_weather(weather_info):
      # Allow the user to query weather information by city
    while True:
        city_query = input("Enter a city name to query the weather (or type 'done' to stop): ")
        
        if city_query.lower() == 'done':  # Stop if the user types 'done'
            break
        
        # Check if the city exists in the weather data
        if city_query in weather_info:
            print(f"\nWeather Information for {city_query}:")
            print(f"  Date: {weather_info[city_query]['date']}")
            print(f"  Temperature: {weather_info[city_query]['temperature']}°C")
            print(f"  Humidity: {weather_info[city_query]['humidity']}%")
            print(f"  Condition: {weather_info[city_query]['weather_condition']}\n")
        else:
            print(f"'{city_query}' not found in the weather data.\n")  
            
weather_info = get_weather_data()  # Get the weather info from the user
query_city_weather(weather_info) 
    
    