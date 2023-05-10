# Write a Python program to print all unique values in a dictionary?
d = {'a':1,'b':2,'c':2,'d':4,'e':1,'f':2}
unique_values = set(d.values())

print("unique values in the dictionry")
for value in unique_values:
    print(value)
