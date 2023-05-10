"""
1) single level inheritance :
      
           A
           |
        ----------  
           |
           B

"""

"""

class person: # Parent Class :
    def input(self,fname,subject):
        self.fname = fname
        self.subject = subject

class faculty(person): # Child Class :
    def display(self):
        print("fname = ",self.fname)
        print("subject = ",self.subject)



f = faculty() # Here Object is called :
f.input("Jay","Python")

f.display() # Here display the class and object :

"""

class A:
    def __init__(self):
        self.num1 = 10
        self.num2 = 20

class B(A):
    def display(self):
        self.ans = self.num1 + self.num2
        print(self.ans)

obj = B()
obj.display()