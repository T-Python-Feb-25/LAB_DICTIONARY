#table for phone book
phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}

phone_number = input("Enter the phone number: ")

#to check the num from user
if not phone_number.isdigit():
    print("This is invalid number.") 
elif len(phone_number) != 10:
    print("This is invalid number.")  
elif phone_number in phone_book:
    print(f"The owner of the number is: {phone_book[phone_number]}")
else:
    print("Sorry, the number is not found.")
