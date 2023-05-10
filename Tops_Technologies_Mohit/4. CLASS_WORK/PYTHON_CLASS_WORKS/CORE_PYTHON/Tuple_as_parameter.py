"""
tuple as a parameter

dictionary as a parameter

"""

# *args and **kwargs

# args : arguments

def myfun(*n1): # arguments
    for i in n1:
        print(i)

myfun(12,23,34,56,8,4,23) # parameters

# kwargs : key with arguments (dictionary)

def myfun(**args):
    for k,v in args.items():
        print(k," ",v)

myfun(name = "anjali",subject = "python")