phoneBook = {"0568323222": "Amal", "0522222232": "Mohammed", "0532335983": "Khadijah",
             "0545341144": "Abdullah","0545534556": "Rawan", "0560664566": "Faisal",
             "0567917077": "Layla"}

phoneNumber= str(input("Please Enter A Phone Number to be checked: "))

def numbervalidityCheck(phoneNumber:str)-> bool:
    count = 0

    for i in phoneNumber:
        count +=1
    if count != 10:
        print ("This is invalid number!")
        return False
    if not phoneNumber.isdigit():
        print("This is invalid number!")
    else :
        if (phoneBook.get(phoneNumber)):
            print(phoneBook.get(phoneNumber))
            return True
        else:
            print("Sorry, the number is not found")
def getName(numberExist:bool):
    if (numberExist):
        print(phoneBook.get(phoneNumber))
numberExist = numbervalidityCheck(phoneNumber)



'''
this is the first Python lab in the Course
Feb8, 2025
By Mohammed Albushaier
'''