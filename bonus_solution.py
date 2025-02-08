"""# Bonus (use a new file)

### Exercise: Weather Data Aggregation

**Objective:** Write a Python program that aggregates weather data for different cities and provides weather data based on user queries.

#### Requirements:

1. **Input Weather Data:** Allow the user to input weather data for different cities. Each entry should include the city name, date, temperature, humidity, and weather condition (e.g., sunny, rainy).
2. **Store Data in a Dictionary:** Use a nested dictionary to store the weather data. The outer dictionary's keys will be the city names, and the values will be another dictionary containing date and weather details.
3. **Query by City:** Allow the user to query the weather data by city name, displaying all the recorded weather data for that city.

#### Guidelines:

- Use nested dictionaries to store the weather data efficiently.
- Implement separate functions for inputting data, querying by city.
- Validate user inputs to ensure correctness.

#### Challenge:

- Extend the program to allow the user to update or delete weather data for a specific city and date.
"""
from datetime import datetime

weather_forecast = {
    "Riyadh": {
        "2025-02-08": [
            {"temperature": 22},
            {"humidity": 45},
            {"weather condition": "Partly Cloudy"},
        ],
        "2025-02-07": [
            {"temperature": 7},
            {"humidity": 50},
            {"weather condition": "Clear Sky"},
        ]
    },
    "Jeddah": {
        "2025-02-08": [
            {"temperature": 28},
            {"humidity": 60},
            {"weather condition": "Clear Sky"},
        ],
        "2025-02-07": [
            {"temperature": 18},
            {"humidity": 67},
            {"weather condition": "Rain"},
        ]
    },
    "Dammam": {
        "2025-02-08": [
            {"temperature": 24},
            {"humidity": 50},
            {"weather condition": "Overcast"},
        ]
    },
    "Khobar": {
        "2025-02-08": [
            {"temperature": 26},
            {"humidity": 55},
            {"weather condition": "Rain"},
        ]
    },
    "Mecca": {
        "2025-02-08": [
            {"temperature": 30},
            {"humidity": 40},
            {"weather condition": "Sunny"},
        ]
    },
}

def records_retreaving():
    city = text_validation("city name").capitalize()
    if city in weather_forecast:
        print("-"*20+f"{city} Records:"+"-"*20)

        for date in weather_forecast[city]:
            print(f"- {date}:")
            for info in weather_forecast[city][date]:
                for key, value in info.items():
                    print(f"  {key}: {value}")
        print("-"*60)
    else:
        print(f"No Records found for {city}")

def data_insertion():
    city = text_validation("city name").capitalize()
    date = date_validation()
    temperature = temp_validation()
    humidity = humidity_validation()
    weather_condition = text_validation("weather condition").capitalize()
    
    if city not in weather_forecast:
        weather_forecast[city] = {}

    if date in weather_forecast[city]:
        print(f"the date {date} already have a forcast.")
    else:
        weather_forecast[city][date] = [
            {"temperature": temperature},
            {"humidity": humidity},
            {"weather condition": weather_condition}
        ]
        print(f"Data for {city} on {date} added successfully.")
    
def update_data():
    city = text_validation("city name").capitalize()
    if city not in weather_forecast:
        print("This city does not have records try to add a new record")
        return
    
    date = date_validation()
    #have a record in that date we will over write
    if date in weather_forecast[city]:
        temperature = temp_validation()
        humidity = humidity_validation()
        weather_condition = text_validation("weather condition")
        weather_forecast[city][date] = [
                {"temperature": temperature},
                {"humidity": humidity},
                {"weather condition": weather_condition}
            ]
    else:
        print("this date does not have a record try to add a new record")

def data_deleation():
    city = text_validation("city name").capitalize()
    
    if city not in weather_forecast:
        print("This city does not have records.")
        return
    
    date = date_validation()
    
    if date in weather_forecast[city]:
        del weather_forecast[city][date]
        print("The record has been deleted successfully.")
        
        if not weather_forecast[city]:  
            del weather_forecast[city]
            
    else:
        print("This date does not have a record.")

def text_validation(text:str)->str:
    valid = False
    while not valid:
        user_input =input(f"Enter the {text}: ")
        if not user_input.isalpha():
            print("Invalid input, cannot contain charecters or numbers")
        else:
            valid=True
    return user_input

def date_validation()->str:
    valid = False
    date_format = "%Y-%m-%d"
    
    while not valid:
        date_input = input("Enter the date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_input, date_format)
            valid = True 
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    return date_input

def temp_validation()->str:
    valid = False
    while not valid:
        temp_input = input("Enter the temperature (in °C): ")
        try:
            temperature = float(temp_input)
            if -100 <= temperature <= 100:
                valid = True  
            else:
                print("Invalid temperature. Please enter a value between -100°C and 100°C.")
        except:
            print("Invalid input. Please enter a numeric value.")
    return temp_input

def humidity_validation()->str:
    valid = False
    while not valid:
        humidity_input = input("Enter the humidity (in %): ")
        try:
            humidity = float(humidity_input)

            if 0 <= humidity <= 100:
                valid = True  
            else:
                print("Invalid humidity. Please enter a value between 0% and 100%.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    return humidity_input

def selection_menu()->str:
    print("1 - Add weather data")
    print("2 - Display city records")
    print("3 - Update weather data")
    print("4 - Delete weather data")
    print("5 - Exit")
    selection= menu_validation()
    return selection

def menu_validation()->str:
    valid = False
    while not valid:
        user_input =input("Enter your choice: ")
        if not user_input.isdigit() or not (1 <= int(user_input) <= 6):
            print("Invalid choice. Please enter a number between 1 and 5.")
        else:
            valid=True
    return user_input


print("-" * 20 + " Welcome to the weather forcast system " + "-" * 20)

while True:

    user_input= selection_menu()
    if user_input=="1":
        data_insertion()
    elif user_input=="2":
        records_retreaving()
    elif user_input=="3":
        update_data()
    elif user_input=="4":
        data_deleation()
    elif user_input=="5":
        break

  


