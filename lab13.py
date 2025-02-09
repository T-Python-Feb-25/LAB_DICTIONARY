phoneBook={"0568323222":"Amal","0522222232":"Mohammed","0532335983":"Khadijah","0545341144":"Abdullah","0545534556":"Rawan","0560664566":"Faisal","0567917077":"Layla"}
phoneNum=int(input("inter your phone number"))
#للتحقق من كون القيم المدخله ارقام و ليست احرف او رموز
if not phoneNum.isdigit():
    print("This is invalid number")

#للتحقق من طول الرقم المطلوب 10
if len (phoneNum) !=10 :
    print("This is invalid number")
#للتحقق من وجودة الرقم في القائمة
for name,number in phoneNum.items():
    if number ==phoneNum:
        print("the owner of this number is {}".format(name))
    else :
        print("Sorry, the number is not found")
