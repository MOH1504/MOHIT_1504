# Write a Python program to read an entire text file?

filename = "example.txt"
with open(filename,"r") as file:
    contents = file.read()
    print(contents)