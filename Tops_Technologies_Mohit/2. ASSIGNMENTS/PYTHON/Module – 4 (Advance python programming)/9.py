# Write a Python program to count the number of lines in a text file?
with open('example9.txt','r') as file:
    lines = file.readlines()
    
    num_lines = len(lines)
    
print("numbers of lines: " , num_lines)    