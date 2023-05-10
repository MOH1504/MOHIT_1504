#Write a Python program to read a file line by line store it into a variable. 
def read_file_to_variable(filename):
    content = ""
    with open(filename,"r") as file:
        content = file.read()
    return content
my_variable = read_file_to_variable("example7.txt")
print(my_variable)    