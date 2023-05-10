""" 
there are 3 types of control statements in python 

1) conditional statement 
2) looping statement 
3) jumping statement 



1) conditional statement 

    -> if statement 
    -> if.. else statement 
    -> elif .. if statement 
    -> nested if statement 

operators : if we want to perform some specific operations 

    at that time we use some specific symbols 

1) Arithmetic : + - * /  ** // 
2) Assignment : to assign a value   (a = 10 )
3) relational operator : >  < >= <= == != 
4) logical operator : and or not 


"""

# if statement / if..else 

# num = int(input("Enter number : "))

# if num>35:
#     print("pass")
# else:
#     print("Fail")


# elif .. statement 

# marks = int(input("Enter marks : "))
# if marks>=70:
#     print("A grade")
# elif marks>=60 and marks<70:
#     print("B grade")
# elif marks>=50 and marks<60:
#     print("C grade")
# elif marks>=40 and marks<50:
#     print("D grade")
# elif marks>30 and marks<40:
#     print("E grade")
# else:
#     print("FAIL")

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


marks = int(input("Enter marks : "))
if marks>=0  and marks <=100:
    if marks>=70:
        print("A grade")
    elif marks>=60 and marks<70:
        print("B grade")
    elif marks>=50 and marks<60:
        print("C grade")
    elif marks>=40 and marks<50:
        print("D grade")
    elif marks>30 and marks<40:
        print("E grade")
    else:
        print("FAIL")
else:
    print("Invalid Input")

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