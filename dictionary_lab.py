## Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner. 
#You can follow the table below:



#- If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
#- If the number is less or more than 10 numbers, print "This is invalid number".
#- If the number contains letters or symbols, print "This is invalid number".
book_number={" Amal ":"0568323222" ,
"Mohammed" : "0522222232 ",
"Khadijah" : " 0532335983 ",
"Abdullah " :"0545341144 ",
"Rawan"  :"0545534556 ",
"Faisal " :"0560664566 ",
"Layla ":" 0567917077 "
}
number =input( " enter the number : ") 

if not number.isdigit():  
  print("invalid pleas enter numbers: ")
elif len(number) !=10:
 print ("please in 10 numbers: " )
else:
 owner = None
for name, number in book_number.items():
        if number == number:
            owner = name
            break
if owner:
         print(f"owner: {owner}")
else:
     print("sorry not found")