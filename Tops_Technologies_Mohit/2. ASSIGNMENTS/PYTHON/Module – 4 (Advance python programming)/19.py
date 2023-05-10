#How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets. 
try:
    x= 10/0
except ZeroDivisionError:
    print("error division by zero")
finally:
    print("this code is always executed")    
     