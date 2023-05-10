"""
Class : class is a collection data type 
        which is contain data member and member function in a single entity.

Object : object is a variable of class

        using of object we can access properties of class.

"""
"""
Class :

       syntax :
        
    Class <classname> :

       data member


       member function

object function :

obj = classname()

"""

"""

class student:
    name = "Jay"
    subject = "Python"

obj = student()
print(obj.name)
print(obj.subject)

"""

"""
Self :which is refer current class properties 

display() : method

difference between function and method 

Function : which is declare outside the class and which is work independent

E.g. : print() , len()

Method : which is dependent on class - and declare inside the class

E.g. : string.toLower() , string.toUpper()

"""
class student:
    name = "Jay"
    subject = "Python"
   
    def display(self):
        print(self.name)
        print(self.subject)
       
obj = student()
obj.display()