#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 
x = int(input("enter the number : "))
y = int(input("enter the number : "))
z = int(input("enter the number : "))

sum = x + y + z
if x == y or y == z or z == x:
    sum = 0
else:
    x + y + z
        
print(sum)        