import re
def input_weather_data():
    '''This function allows users to input weather data for a city,date,temperature,humidity,weather condition. with validate user input and prevent duplaicte'''
    global Weather_Data
    pattern=r"^\d{4}/\d{2}/\d{2}$"
    city=input("Enter city name: ")
    if city not in Weather_Data:
        Weather_Data[city]={}
    while True:
        date=input("Enter the date (YYYY/MM/DD) in the same format: ")
        if re.match(pattern,date):
            if date in Weather_Data[city]:
                print("The weather data for this date already exists.")
                return
        else:
            print("Invalid date. Please enter a valid date.")
            return
        
        temp=input("Enter the temperature (only digits):")
        humidity=input("Enter the humidity (only digits): ")
        Weather_condition=input("Enter the weather condition (only letters): ")
        if not temp.isdigit() or not humidity.isdigit() or not Weather_condition.isalpha():
            print("please try again")
        else:
            Weather_Data[city][date]={}
            Weather_Data[city][date]["temp"]=temp
            Weather_Data[city][date]["humidity"]=humidity
            Weather_Data[city][date]["Weather_condition"]=Weather_condition
            break
def querying_by_city(city):
    '''This function allows users to query and display all weather data for a specific city.
       args:
           city(string):the name of the city for which the weather data is to be queried
       '''
    if city in Weather_Data: 
        city_data=Weather_Data[city]
        print(f"weather information for {city.capitalize()}")

        for k,v in city_data.items():
            print(f"date: {str(k).strip("{''}")}")
            print(f"Temperature: {str(city_data[k]['temp']).strip("{''}")}")
            print(f"humidity: {str(city_data[k]['humidity']).strip("{''}")}%")
            print(f"Weather_condition: {str(city_data[k]['Weather_condition']).strip("{''}")}")
            print("-"*20)
def update_data_by_city_and_date(city,date):
       '''This function allows users to update the weather data for a specific city and date. It allows changing temperature, humidity , weather condition.
          args:
              city (string): The name of the city where the data needs to be updated.
              date (string): The date for which the weather data should be updated.
          '''
       if city not in Weather_Data:
           print(f"No weather data found for the city '{city.capitalize()}'.")
           return
       else:
            if date not in Weather_Data[city]:
                print(f"No weather data found on the date '{date}'.")
                return
            else:
                temp=input("Enter the temperature (only digits):")
                humidity=input("Enter the humidity (only digits): ")
                Weather_condition=input("Enter the weather condition (only letters): ")
                if not temp.isdigit() or  not humidity.isdigit() or not Weather_condition.isalpha():
                    print("please try again")
                else: 
                    Weather_Data[city][date]["temp"]=temp
                    Weather_Data[city][date]["humidity"]=humidity
                    Weather_Data[city][date]["Weather_condition"]=Weather_condition
def delate_data_by_city_and_date(city,date):
      '''This function allows users to delete weather data for a specific city and date from the Weather_Data dictionary.
         args:
            city (string): The name of the city from which the weather data should be deleted.
            date (string): The date for which the weather data should be deleted.'''
      if city not in Weather_Data:
           print(f"No weather data found for the city '{city.capitalize()}'.")
           return
      else:
            if date not in Weather_Data[city]:
                print(f"No weather data found on the date '{date}'.")
                return
            else:
                Weather_Data[city].pop(date, None)



                    
    
Weather_Data={}
    
while True:
    user_input = input("""
If you want to add data, enter: 1
If you want to search for data, enter: 2
If you want to update data, enter: 3
If you want to delete data, enter: 4
If you want to exit, enter: 5
""").strip()
    if user_input=='1':
    
        input_weather_data()
    elif user_input=='2':
        user_input_city = input("Enter the city name: ").strip()
        querying_by_city(user_input_city)
    elif user_input=='3':
        print("To update the weather data, please enter the city name and the date (in YYYYMMDD format).")
        user_input_city  = input("Enter the city name: ").strip()
        user_input_date = input("Enter the date (YYYYMMDD): ").strip()
        update_data_by_city_and_date(user_input_city,user_input_date)
    elif user_input=='4':
        user_input_city  = input("Enter the city name: ").strip()
        user_input_date = input("Enter the date (YYYYMMDD): ").strip()
        delate_data_by_city_and_date(user_input_city,user_input_date)
    elif user_input=='5':
        break
    else:
        print("Invalid number. Please enter a valid number.")




        
        




