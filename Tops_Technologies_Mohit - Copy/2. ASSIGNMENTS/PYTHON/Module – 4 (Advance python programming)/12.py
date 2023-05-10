#Write a Python program to copy the contents of a file to another file?
with open ('input12.txt','r') as input12_file, open ('output12.txt','w') as output12_file:
    countents = input12_file.read()
    output12_file.write(countents)