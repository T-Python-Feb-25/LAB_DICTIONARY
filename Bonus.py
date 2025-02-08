city_name=input("Enter the city name:")
date= input("Enter the data:")
temperature = input("Enter the  temperature: ")
humidity = input("Enter the temperature for humidity:")
weather_condition = input("Enter the temperature for weather_condition:")
citys = {
    'Riyadh': {
        'name': 'Riyadh',
        'date': '12/11/2024',
        'temperature': '33°C',
        'humidity': '20%',
        'weather_condition': 'Sunny',
    },
    'Jeddah': {
        'name': 'Jeddah',
        'date': '12/11/2024',
        'temperature': '29°C',
        'humidity': '65%',
        'weather_condition': 'Cloudy',
    },
    'Mecca': {
        'name': 'Mecca',
        'date': '12/11/2024',
        'temperature': '37°C',
        'humidity': '30%',
        'weather_condition': 'Hot & Sunny',
    },
    'Dammam': {
        'name': 'Dammam',
        'date': '12/11/2024',
        'temperature': '28°C',
        'humidity': '50%',
        'weather_condition': 'Hazy',
    },
    'Abha': {
        'name': 'Abha',
        'date': '12/11/2024',
        'temperature': '18°C',
        'humidity': '70%',
        'weather_condition': 'Rainy',
    }
}
city_name = input("Enter the city name to you want the updated temperature: ")
new_temperature = input("Enter the new temperature: ")

if city_name in citys:
    data = citys[city_name]
    print(f"Weather data for {city_name}:")
    print(f"Date: {data['date']}")
    print(f"Temperature: {data['temperature']}")
    print(f"Humidity: {data['humidity']}")
    print(f"Weather Condition: {data['weather_condition']}")

else:
    print("Sory the weather is not found")


if city_name in citys:
    citys[city_name]['temperature'] = new_temperature
    print(f"Updated temperature for {city_name}: {new_temperature}")
else:
    print("City not found")

if city_name in citys:
    del citys[city_name]
    print(f"Deleted weather data for {city_name}")

else:
    print("City not found")
