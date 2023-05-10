"""
1) Hierarchical inheritance :
 
           A
           |
           V
    -----------------
    |               |
    B               C

"""

"""
class person: # Parent Class :- Base Class
    def input1(self,fname,subject):
        self.fname = fname
        self.subject = subject

class faculty(person): # Child Class :- Derive Class
    def display(self):
        print("fname = ",self.fname)
        print("subject = ",self.subject)

class student(person): # Child Class :- Derive Class
    def display(self):
        print("fname = ",self.fname)
        print("subject = ",self.subject)



f = input("Enter Name : ")
s = input("Enter Subject : ")

f1 = faculty()
f1.input1(f,s)
f1.display()

f = input("Enter Name : ")
s = input("Enter subject : ")

s1 = student()
s1.input1(f,s)
s1.display()

"""

class A:
    def inputA(self):
        self.a = 10
        self.b = 20

    def displayA(self):
        print(self.a)
        print(self.b)

class B(A):
    def inputB(self):
        self.c = 30
        self.d = 20

    def displayB(self):
        self.ans = self.a + self.b + self.c + self.d
        print("Ans = ",self.ans)

class C(A):
    def multiplication(self):
        print(self.a * self.b)

obj = B()
obj.inputA()
obj.inputB()
obj.displayA()
obj.displayB()

obj = C()
obj.inputA()
obj.multiplication()

