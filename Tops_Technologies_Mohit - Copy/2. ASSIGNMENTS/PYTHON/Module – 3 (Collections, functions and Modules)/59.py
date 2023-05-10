#Write a Python program to convert degree to radian?
import math
def degree(degree):
    return degree * (math.pi / 180)

degree = float(input("enter degree:"))
radian = degree(degree) 
print("radian:", radian )   