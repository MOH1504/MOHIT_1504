# Write a Python program to read first n lines of a file?
filename = "example4.txt"
n = 5
with open (filename,"r") as file:
    lines  = file.readline()
    for line in lines[:n]:
        print(line.strip())