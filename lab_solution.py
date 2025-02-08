#Lab Solution Sabreen Binsalman
## Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner. 
#- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
#- If the number is less or more than 10 numbers, print "This is invalid number".
#- If the number contains letters or symbols, print "This is invalid number".

phone_book={"0595543693":"Sabreen",
            "0568323222":"Amal",
            "0522222232":"Mohammed",
            "0532335983":"Khadijah",
            "0545341144":"Abdullah",
            "0545534556":"Rawan",
            "0560664566":"Faisal",
            "0567917077":"Layla"}

invalid_input=True

print("-" * 20 + " Welcome to The Phone Book System " + "-" * 20)

while invalid_input:
    user_input=input("Please enter the number (e.g. 0596653934) : ")
    if len(user_input)==10 and user_input.isdigit() and user_input.startswith("05"):    
        invalid_input=False
        if user_input in phone_book:
            name = phone_book[user_input]
            print(f"The owner of this number is {name}")
        else:
            print("Sorry, the number is not found")
    else:
        print("This is invalid number.. try again")


        



