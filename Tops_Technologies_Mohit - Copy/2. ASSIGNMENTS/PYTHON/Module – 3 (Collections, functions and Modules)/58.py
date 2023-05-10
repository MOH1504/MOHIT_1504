#  Write a Python program to read a random line from a file.
import random 

f = open ("C:\\Users\\Lenovo\\Desktop\\assignment\\python module 3\\read.txt",'r')

lines = f.read().splitlines()

print(lines)
print(lines[0])

print(random.choice(lines))