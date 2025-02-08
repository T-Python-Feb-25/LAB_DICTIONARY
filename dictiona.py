phone_directory = {
    "Amal":       "0568323222",
    "Mohammed":   "0522222232",
    "Khadijah":   "0532335983",
    "Abdullah":   "0545341144",
    "Rawan":      "0545534556",
    "Faisal":     "0506645666",
    "Layla":      "0567917077"
}

entered_number = input("Enter the phone number: ")

if not entered_number.isdigit():
    print("This is invalid number")
elif len(entered_number) != 10:
    print("This is invalid number")
else:
    is_found = False
    for person_name, person_number in phone_directory.items():
        if person_number == entered_number:
            print(f"The owner of the number is: {person_name}")
            is_found = True
            break
    if not is_found:
        print("Sorry, the number is not found.")
