phone_number = input("Enter your phone number:")
my_dictionary = {
    "Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadija": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077"

}

if len(phone_number) != 10 and not phone_number.isdigit():
    print("This is invalid number")
    exit()


number_found = False
for key, value in my_dictionary.items():
    if value == phone_number:
        print(f"the owner :{key}")
        number_found = True
        break

if not number_found:
    print("Sorry, the number is not found")
