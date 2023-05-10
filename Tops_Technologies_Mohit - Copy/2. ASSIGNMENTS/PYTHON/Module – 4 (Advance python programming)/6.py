# Write a Python program to read a file line by line and store it into a list?
def file(filename):
    line = []
    with open(filename,"r") as file:
        for line in file:
            line.append(line.strip())
    return line
my_list = file("example6.txt") 
print(my_list)      
        