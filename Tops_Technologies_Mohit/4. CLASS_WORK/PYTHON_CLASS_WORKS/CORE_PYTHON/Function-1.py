"""
3). function without parameters and fuction with return types.

syntax : 

def myfun():
    statement

"""
# def checkEvenOdd():
#     num = int(input("Enter your number : "))
#     if num%2 == 0:
#         return "Even number"
#     else:
#         return "Odd number"

# print(checkEvenOdd())

"""
4). fuction with parameters and function with return types :

"""
def checkEvenOdd(num):
    
    if num%2 == 0:
        return "Even number"
    else:
        return "Odd number"

num = int(input("Enter your number : "))
print(checkEvenOdd(num))









