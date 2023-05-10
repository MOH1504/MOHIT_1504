"""
1) Multiple inheritance : 

     A                B
     |                |   ----->>>> TWo base class and One derive class.
     |                |
     ------------------
            |
            |
            C

"""

class A:
    def inputA(self,num1):
        self.num1 = num1

class B:
    def inputB(self,num2):
        self.num2 = num2

class C(A,B):
    def display(self):
        self.ans = self.num1 + self.num2
        print(self.ans)

obj = C()
obj.inputA(12)
obj.inputB(23)
obj.display()