"""
__init__.py : if we put this file in blank folder it will consider as package.

__init__() : this is a function.

which is similar like constructor

by default it call automatic once object of class create.

"""
 
class student:
    def display(self): # Method called
        print("this is student class")

student = student()
student.display()


class Faculty:
    def __init__(self): # Constructor called
        print("this is faculty constructor")

faculty = Faculty()