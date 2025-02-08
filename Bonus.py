#Weather Data Aggregation

weatherData={}

def addWeatherDate():
    city = input("Please enter city name: ")
    date = str(input("Please enter the date (DD-MM-YYYY): "))
    temperature = input("Please enter the temperature in (°C): ")
    humidity_level = input("Please enter the humidity level (%): ")
    condition = input("Please enter the condition (e.g., sunny, rainy)")
    if city and date and temperature.isnumeric() and humidity_level.isnumeric() and condition:
        weatherData[city]={}
        weatherData[city][date]={
            "temperature":float (temperature),
            "humidity" : float(humidity_level),
            "condition" : condition
        }
        print("Weather data added successfully.")


def queryWeatherData():
    city=input("Enter city name to query: ")
    if city in weatherData:
        print(f"Weather data for {city}:")
        for date, details in weatherData:
           print (f"Date: {date}, temperature: {date['temperature']}C, humidity: {date['humidity']}% "
                  f"condition: {date['condition']}")
    else :
        print ("No data found for that city.")

def deleteWeatherData():
    city = input("Please enter city name you would like to delete from: ")
    date = input("Please enter the date (DD-MM-YYYY) of the record to delete: ")

    if city in weatherData and date in weatherData[city]:
        deleteWeatherData([city][date])
        print (f"Weather data of {city} deleted successfully.")
        if not weatherData[city]:
            del weatherData[city]
            print(f"No record of {city} was found")

def main():
    while True:
        print ("\n Welcome to the Weather application")
        print ("1- To add new city weather data ")
        print ("2- To query about city weather data")
        print ("3- To Delete a city weather data")
        print ("7- To Exit the app")
        choice = int(input("Please select an option from the list above \n"))

        if choice ==1:
            addWeatherDate()
        elif choice == 2:
            queryWeatherData()
        elif choice ==3:
            deleteWeatherData()
        elif choice ==7:
            print("Exiting the application")
            break
        else:
            print("Invalid option, Please try again")

main()
'''
this is the first Python lab in the Course
Feb8, 2025
By Mohammed Albushaier
'''