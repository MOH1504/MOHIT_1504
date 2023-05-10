num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

if num1 >= 0 or num2 >= 0:
    print("number is positive : ")
elif num1 == 0 or num2 == 0:
    print("number is zero : ")
else:
    print("number is negative : ")