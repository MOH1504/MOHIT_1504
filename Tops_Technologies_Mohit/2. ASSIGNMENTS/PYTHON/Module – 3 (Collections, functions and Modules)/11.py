"""
Write a Python function that takes a list and returns a new list with unique
elements of the first list. 
"""

def unique_list(l):
    unique = []
    for item in l:
        if item not in unique:
            unique.append(item)
    return unique
print("unique num :")
print(unique_list([1,2,4,5,2,4,6,4,8,5])) 