numbers_and_names={"0568323222":"Amal","0522222232":"Mohammed","0532335983":"Khadijah","0545341144":"Abdullah","0545534556":"Rawan","0560664566":"Faisal","0567917077":"Layla"}

while True:
    user_input=input('Enter a number (type e to exit): ')
    if user_input =="e":
        break
    if len(user_input)!=10:
        print("This is invalid number")
    elif not user_input.isdigit():
        print("This is invalid number")

    
    else:
        if user_input in numbers_and_names:
            print(numbers_and_names[user_input])
        else:
            print("Sorry, the number is not found")
            
