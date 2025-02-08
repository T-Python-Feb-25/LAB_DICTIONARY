

def find_owner():
    
    phone_book = {
        "0568323222": "Amal",
        "0522222232": "Mohammed",
        "0532335983": "Khadijah",
        "0545341144": "Abdullah",
        "0545534556": "Rawan",
        "0560664566": "Faisal",
        "0567917077": "Layla"}
    
    phone_number = input("Enter a phone number:")
    
    if phone_number in phone_book:
        return phone_book[phone_number]
    elif len(phone_number)> 10:
        print("This is invalid number")
    elif any(not char.isdigit() for char in phone_number):
        print("This is invalid number")
    else:
        return "Owner not found"

sear = find_owner()
print(sear)

    