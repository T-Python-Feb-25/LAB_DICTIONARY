

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
    findnum = input("Enter the phone number you want to find: ")

    if findnum.isdigit() and len(findnum) == 10:
        if findnum in phone_book:
            print(f"name of this phone number: {phone_book[findnum]}")
            break
        else:
            print("Number not in phone book.")
    else:
        print("This is invalid number, please try again.")







