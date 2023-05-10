#Write a Python class named Circle constructed by a radius and two methods which will compute 
# the area and the perimeter of a circle ?
class circle:
    def __init__(self,radius):
        self.radius =radius
        def area (self):
            return 3.14 * self.radius  ** 2
        def perimeter(self):
            return 2 * 3.14 ** self.radius
    my_circle = circle(5)
    area = my_circle.area()
    perimeter = my_circle.perimeter()
print("the area of circle is : ",area)
print("the perimeter of my circle is perimeter : ", perimeter)
            