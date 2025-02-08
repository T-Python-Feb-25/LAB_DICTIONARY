phone_book = {
    "Amal": "0568323222",
    "Mohammad": "0522222189",
    "Khadijah": "0532666691",
    "Abdullah": "0541123663",
    "Rawan": "0552332956",
    "Faisal": "052282153",  
    "Layla": "0563236698"
}

name = input("Enter the name to get the phone number: ")
if name in phone_book:
    print(f"{name}'s phone number is {phone_book[name]}")
else:
    print("Sorry, the name is not found")

number = input("Enter the phone number to find the owner: ")
if number.isdigit() and len(number) == 10:
    if number in phone_book.values():
        owner = [name for name, phone in phone_book.items() if phone == number][0]
        print(f"The owner of the number {number} is {owner}")
    else:
        print("Sorry, the number is not found")
else:
    print("This is an invalid number")

