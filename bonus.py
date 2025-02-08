def input_weather_data():
     '''
     Prompts the user to input weather data for multiple cities.
     
     Args:
        No Args
     Returns:
        dict: A dictionary containing weather data for the cities entered by the user.

     '''

     while True:
        NoOfCities = input("How Many Number Of Cities Do you Want To Enter: ")
        if NoOfCities.isdigit():
            NoOfCities = int(NoOfCities)
            break
        else: 
            print("Not A Number")
         
     weather_data = {}

     while(NoOfCities != 0):

        while True: 
            city = input("Enter The City Name: ")
            if city.isalpha():
                 break
            else:
                print("Enter Valid Name")
        date = input("Enter The Date: ")

        while True:
            try:
                temperature = float(input("Enter The Temperature: "))
                break
            except ValueError:
                print("Enter A Valid Number")
     
        while True:
            try:
                humidity = float(input("Enter The humidity: "))
                break
            except ValueError:
                print("Enter A Valid Number")

        while True:
            weatherCondition = input("Enter The Weather Condition: ")
            if weatherCondition.isalpha():
                break
            else:
                print("Enter A Valid Number")
        data = {
            "date": date,
            "temperature": temperature,
            "humidity": humidity,
            "weatherCondition": weatherCondition
        }


        weather_data[city] = data
        print("City Added Successfully\n")

        NoOfCities-=1
     return weather_data  

def queryCity(cityName, dic):
     '''
     Queries the weather data for a specified city.

     Args:
        cityName (str): The name of the city to query.
        dic (dict): The dictionary containing weather data for multiple cities.
     Returns:
        None: This function print the result
     '''
     if cityName in dic:
          print(f"All Data for {cityName} City")
          print(f"Date: {dic[cityName]["date"]}")
          print(f"Temperature: {dic[cityName]["temperature"]}")
          print(f"Humidity: {dic[cityName]["humidity"]}")
          print(f"Weather Condition: {dic[cityName]["weatherCondition"]}\n")
     else: 
          print("No Recorded Data For This City")


def modifyWeather(cityName, dic):
    """
    Modifies the weather data for a specified city.

    Args:
        cityName (str): The name of the city whose weather data is to be modified.
        dic (dict): The dictionary containing weather data for multiple cities.
    Returns:
        None: This function print the result
    """
    print("Modify City")
    if cityName in dic:
        dic[cityName]["date"] = input("Enter The Date: ")
        dic[cityName]["temperature"] = input("Enter The temperature: ")
        dic[cityName]["humidity"] = input("Enter The humidity: ")
        dic[cityName]["weatherCondition"] = input("Enter The weather condition:")
        print(dic)
    else:
        print("No Recorded Data For This City")



def deleteWeather(cityName, dic):
    '''
    Deletes the weather data for a specified city.

    Args:
        cityName (str): The name of the city to delete weather data for.
        dic (dict): The dictionary containing weather data for multiple cities.
    Returnn:
        None: This function print the result
    '''
    print("Delete City")
    if cityName in dic:
        del dic[cityName]
        print(f"After Deleation {dic}")
    else: 
        print("No Recorded Data For This City")



allData = input_weather_data()
queryCity("Riyadh",allData)
deleteWeather("Jeddah",allData)
modifyWeather("Makkah",allData)
