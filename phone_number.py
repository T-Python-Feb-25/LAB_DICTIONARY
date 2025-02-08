numbers = input("Please Enter the phone number") .strip() # input the number from the user

#Creat a dicctionary 
phone_book = {
    "0568323222" : "Amal",
    "0522222232" : "Mohammed",
    "0532335983" : "Khadijah",
    "0545341144" : "Abdullah", 
    "0545534556" : "Rawan", 
    "0560664566" : "Faisal",
    "0567917077" : "Layla",
}

#
if len(numbers) != 10 or not numbers.isdigit():
    print("This is an invalid number.")
else:
    if numbers in phone_book:
        owner_name = phone_book[numbers]
        print(f"Owner name: {owner_name}")
    else:
        print("Sorry, the number is not found.") 





