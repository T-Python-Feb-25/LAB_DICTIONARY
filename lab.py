userInput = input("Enter Phone Number: ")

while (len(userInput) != 10 or not userInput.isdigit()):
    print("This is invalid number")
    userInput = input("Enter Phone Number: ")

def phone_book(phoneNumber):
    '''
    This function takes a phone number and look if it is exsist
   
    Args: 
        phoneNumber (str): Phone Number you want to search for 

    Returns:
        None: This function print the result
    '''
    dictionary = {
        "0568323222": "Amal",
        "0522222232": "Mohammed",
        "0532335983": "Khadijah",
        "0545341144": "Abdullah",
        "0545534556": "Rawan",
        "0560664566": "Faisal",
        "0567917077": "Layla",
    }

    if phoneNumber in dictionary:
        print(dictionary[phoneNumber])
    else: 
        print("Sorry Not Found")


phone_book(userInput)