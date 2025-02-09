
phone_book1 = {
    "Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077"
}
phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}

def find_owner(number):
    if not number.isdigit() or len(number) != 10:
        return "This is an invalid number."
    return phone_book.get(number, "Sorry, the number is not found.")

user_number = input("Enter a phone number: ")
while user_number != "0":
    print(find_owner(user_number))
    user_number = input("Enter a phone number (0 to exit): ")
