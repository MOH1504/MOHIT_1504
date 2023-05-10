"""
Function : function is a block of code that code are used to again and again using of function we can reduce our code
            using of function we can reuse our code.

How we can use function

there are 2 steps :

1) function declaration : 
2) function defination :
3) function calling :

for python 
syntax :

1) function define 
        which is contain block of code 

        def funname():
            block of code

2) function calling :
        when we want to use this function
         
        funname()

"""
#  1) function without parameters and function without return type

        # def funname():
           # block
def greetings(): # function define
    print("hello welcome to python")

greetings()   # function calling

"""
Function categories :

    there are 4 types of function categories 

    1) function without parameters and function without return type

        def funname():
            block


"""


"""
2) function with parameter and without return type
           block of code
"""

def addition(num1,num2):
    ans = num1 + num2
    print(ans)

addition(12,23)

n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))

addition(n1,n2)