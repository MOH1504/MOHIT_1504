#Explain Exception handling? What is an Error in Python? 
"""Exception handling is a programming construct in Python that allows you to gracefully 
   handle errors that may occur during program execution. When an error occurs in Python, 
   an exception object is raised that describes the type of error and where it occurred in the code. 
   If the exception is not handled by the program, it will result in the program terminating and 
   displaying a traceback message that shows the line of code where the error occurred.
"""
try:
    
    with open ("example13.txt", 'r') as file:
      contents = file.read()
except FileNotFoundError:
    print("file not found")
        