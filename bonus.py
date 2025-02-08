'''Bonus (use a new file)
Exercise: Weather Data Aggregation
Objective: Write a Python program that aggregates weather data for different cities and provides weather data based on user queries.

Requirements:
Input Weather Data: Allow the user to input weather data for different cities. Each entry should include the city name, date, temperature, humidity, and weather condition (e.g., sunny, rainy).
Store Data in a Dictionary: Use a nested dictionary to store the weather data. The outer dictionary's keys will be the city names, and the values will be another dictionary containing date and weather details.
Query by City: Allow the user to query the weather data by city name, displaying all the recorded weather data for that city.
Guidelines:
Use nested dictionaries to store the weather data efficiently.
Implement separate functions for inputting data, querying by city.
Validate user inputs to ensure correctness.
Challenge:
Extend the program to allow the user to update or delete weather data for a specific city and date.'''

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
weather= get_weather_data()
print(weather)
    
    