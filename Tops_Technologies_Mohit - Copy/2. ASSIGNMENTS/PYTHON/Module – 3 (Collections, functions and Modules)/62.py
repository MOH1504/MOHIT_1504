#Write a Python program to calculate surface volume and area of a cylinder?
import math
def cylinder_surface_area(radius,height):
    return 2 * math.pi * radius * (radius+height)
def cylinder_volume(radius,height):
    return math.pi * radius *radius *height
radius = float(input("enter the radius of cylinder : "))
height = float(input("enter the height of cylinder"))

surface_area = cylinder_surface_area(radius,height)
volume = cylinder_volume(radius,height)


print("surface area : ",surface_area)
print("volume : ", volume)