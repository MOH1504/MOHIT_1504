#Write a Python class named Rectangle constructed by a length and width and a method which will compute the 
# area of a rectangle?

class rectangle:
    def __init__ (self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length  * self.width
my_rectangle = rectangle(10,5) 
area = my_rectangle.area()
print("the area of my rectangle is : ", area)   