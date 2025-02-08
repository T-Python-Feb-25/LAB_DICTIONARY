
def input_weather_data(w:int,weather:dict):
    """adding weather data to weather dictionary
    :arg
    w:how many city the user wants to add
    weather:weather dictionary
    :return
    none
    """
    for i in range(w):
        while True:
            city = input("What is city name? ")
            weather_con= input("What is the weather condition? sunny, rainy or cloudy? ")
            date = input("What is the date?")
            temp = input("What the temperature? ")
            humidity = input("What is the humidity? 1-100: ")

            if not city.isalpha() or not weather_con.isalpha() :
                print("Please enter a valid city,  weather condition!!")
                continue
            if not  humidity.isdigit() or not temp.isdigit():
                print("Humidity must be between 1 and 100. and temperature must be between -50 and 100.")
                continue
            if date == "":
                print("Please enter a valid date!")
                continue
            else:
                weather[city] = {"date": date,
                                 "temperature": temp,
                                 "humidity": humidity,
                                 "weather_condition": weather_con
                                 }
                break


def findCity(city: str, weather: dict):
    """
    looking for a city in a given weather dictionary

    :param city: the city to look for
    :param weather: thw weather dictionary
    :return:
    prints city info if found
    """
    if city in weather:
        print(f"Weather details for {city} {weather[city]}:")
    else:
        print(f"{city} not found in the weather data.")



def editcity(city: str, weather: dict):
    """
    updating info in an existing city
    :param city: city to edit
    :param weather: weather dictionary
    :return:
    none
    """
    if city in weather:
        while True:
            choice=input("do you want to (1) update the city or (2) delete the city: ")
            if choice == "1":
                print(f"add the new elements you want to change to {city}: ")
                weather_con = input("What is the weather condition? sunny, rainy or cloudy? ")
                date = input("What is the date?")
                temp = input("What the temperature? ")
                humidity = input("What is the humidity? 1-100: ")
                weather[city].update({"date": date,
                                      "temperature": temp,
                                      "humidity": humidity,
                                      "weather_condition": weather_con})
                break
            if choice == "2":
                del weather[city]
                break

            else:
                print("Please enter a valid number")







weather = {}

cities =int(input("how many cities your adding? "))

input_weather_data(cities,weather)

while True:
    choice = input("Would you like to (1) looking for a city, (2) update or delete a city,(3) print the weather info or (4) Exit? ")

    if choice == "1":
        c = input("Enter the city you are looking for: ")
        findCity(c, weather)
    elif choice == "2":
        c = input("Enter the city you would like to update or delelte: ")
        editcity(c, weather)
    elif choice == "3":
        print(weather)
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")








