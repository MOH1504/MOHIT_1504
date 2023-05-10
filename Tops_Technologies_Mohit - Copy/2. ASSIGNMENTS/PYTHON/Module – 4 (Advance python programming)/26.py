#Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Some generic sound")
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
    
    def make_sound(self):
        print("Woof!")
        
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, species="Cat")
    
    def make_sound(self):
        print("Meow!")
my_dog = Dog("Fido", "Labrador Retriever")
my_cat = Cat("Whiskers")

print(my_dog.name)  
print(my_dog.species) 
my_dog.make_sound()  

print(my_cat.name)  
print(my_cat.species)  
my_cat.make_sound()  
