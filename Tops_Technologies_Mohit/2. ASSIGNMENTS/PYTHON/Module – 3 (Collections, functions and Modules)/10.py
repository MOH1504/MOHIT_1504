"""
Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30. 
"""

squared_numbers = [i**2 for i in range(1, 31)]
first_five = squared_numbers[:5]
last_five = squared_numbers[-5:]

print("First five elements:", first_five)
print("Last five elements:", last_five)