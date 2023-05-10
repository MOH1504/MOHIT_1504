"""
---->>>>> Multi-level inheritance :

     A : Grand parent
     |
     B : Parent
     |
     C : Child

"""

"""

class Gov:
    def intro(self):
        print("WELCOME TO INDIAN GOV.")

class RBI(Gov):
    def guidelines(self):
        print("8.5% rate")

class SBI(RBI):
    def roi(self):
        print("SBI")

sbi = SBI()
sbi.intro()
sbi.guidelines()
sbi.roi()

"""

class A:
    def add(self):
        self.num1 = 10
        self.num2 = 20

class B(A):
    def multiplication(self):
        self.num3 = 5
        self.num4 = 2

class C(B):
    def display(self):
        self.add = self.num1 + self.num2
        self.multiplication = self.num3 * self.num4
        print("Addition = ",self.add)
        print("Multiplication = ",self.multiplication)

c = C()
c.add()
c.multiplication()
c.display()
 


        
