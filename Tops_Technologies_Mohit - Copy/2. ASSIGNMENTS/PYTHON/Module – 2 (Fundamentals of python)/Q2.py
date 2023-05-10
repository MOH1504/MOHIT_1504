#Write a Python program to get the Factorial number of given number. 
num = int (input("enter a number : "))
factorial = 1
if num < 0:
    print ("sorry, factorial does not exit for nagitive number")
    
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial * i
    print("The factorial of", num,"is",factorial)    