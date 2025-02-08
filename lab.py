
phone_book = {
    "Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077",
}

phone_check = input(" Provide the number: ")

if not phone_check.isdigit() or len(phone_check) != 10:
    print("This is an invalid number.")
else:
    if phone_check in phone_book.values():
        owner = [name for name, number in phone_book.items() if number == phone_check][0]
        print(f"The owner of the number {phone_check} is {owner}.")
    else:
        print("Sorry, the number is not found. ")