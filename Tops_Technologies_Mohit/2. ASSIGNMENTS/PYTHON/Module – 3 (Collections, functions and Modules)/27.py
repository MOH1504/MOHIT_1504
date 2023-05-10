#Write a Python program to find the repeated items of a tuple. 
from collections import Counter
numbers = (1,2,3,4,5,6,7,8,8,1,2,3,5)
counts = Counter(numbers)
repeated_item = [item for item , count in counts.items() if count > 1]

print(f"the repeated item are: {repeated_item}")