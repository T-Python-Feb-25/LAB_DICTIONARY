#Creat dictionary to store weather
weather_data = {}

#Show user list
while True:
    print("\n1. Add Weather Data")
    print("2. View Weather Data")
    print("3. Update Weather Data")
    print("4. Delete Weather Data")
    print("5. Exit")
    
    choice = input("Choose an option: ")

#Add weather data 
    if choice == "1":
        city = input("Enter city name: ")
        date = input("Enter date: ")
        temp = input("Enter temperature: ")
        humidity = input("Enter humidity: ")
        condition = input("Enter condition: ")

        if city not in weather_data:
            weather_data[city] = {}

        weather_data[city][date] = {
            "temp": temp,
            "humidity": humidity,
            "condition": condition
        }
        print("Data added.")

    elif choice == "2":
        city = input("Enter city name: ")
        if city in weather_data:
            for date, info in weather_data[city].items():
                print(f"{date}: {info['temp']}C, {info['humidity']}%, {info['condition']}")
        else:
            print("No data found.")

    elif choice == "3":
        city = input("Enter city name: ")
        if city in weather_data:
            date = input("Enter date to update: ")
            if date in weather_data[city]:
                temp = input("Enter new temperature: ")
                humidity = input("Enter new humidity: ")
                condition = input("Enter new condition: ")
                weather_data[city][date] = {
                    "temp": temp,
                    "humidity": humidity,
                    "condition": condition
                }
                print("Data updated.")
            else:
                print("Date not found.")
        else:
            print("City not found.")

    elif choice == "4":
        city = input("Enter city name: ")
        if city in weather_data:
            date = input("Enter date to delete: ")
            if date in weather_data[city]:
                del weather_data[city][date]
                if not weather_data[city]:
                    del weather_data[city]
                print("Data deleted.")
            else:
                print("Date not found.")
        else:
            print("City not found.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")