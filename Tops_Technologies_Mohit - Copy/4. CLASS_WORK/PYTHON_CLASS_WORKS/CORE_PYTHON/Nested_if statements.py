# nested if statement 

"""
if condition:
    statement 
    if condition:
        statement 
    else:
        statement 

else:
    if condition:
        statement 
"""

#--------------- find greatest number among three numbers 


num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))

if num1>num2:
    if num1 > num3:
        print("Number 1 is greater")
    else:
        print("Number 3 is greater")
else:
    if num2 > num3:
        print("number 2 is greater")
    else:
        print("Number 3 is greater")