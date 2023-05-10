#How to Define a Class in Python? What Is Self? Give An Example Of A Python Class ?
"""To define a class in Python, you can use the class keyword followed by the name of the class. 
The code inside the class should be indented, and it typically contains class variables, instance variables, 
methods, and a special method called __init__().

self is a special parameter in Python that refers to the instance of the class. 
It is used to access the instance variables and methods within the class"""

class car:
    wheels = 4
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        
    def description(self):
        print(f"this car is a {self.make}{self.model}{self.year} with {self.wheels} wheels. ")   
        
my_car = ["honda", "civic", 2020]
print(my_car.make)
print(my_car.description())        
        
