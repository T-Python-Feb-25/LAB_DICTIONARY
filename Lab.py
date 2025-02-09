
phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}

while True:
    phone_number = input("Enter the phone number: ")


    if not phone_number.isdigit():  
        print("This is invalid number. pleas enter number that does not contains letters or symbols)")
    elif len(phone_number) != 10:
        print("This is invalid number. the phone number must be 10 digits")
    elif phone_number in phone_book:
        print(f"The owner of this number is: {phone_book[phone_number]}")
        break
    else:
        print("Sorry, the number is not found.")
        break
