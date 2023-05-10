#Write a Python program to calculate the area of a parallelogram ?
def  area(base, height):
    return base  * height
base = float(input("enter the length of the base : "))
height = float(input("enter the height of the parallelogram : "))

area = area(base,height)
print("the area of parallelogram is : ", area)