#Write a Python program to check whether an element exists within a tuple?
numbers = (1,2,3,4,5,6,7)
search_element = 8
if search_element in numbers:
    print(f"{search_element} exists in the tuple")
else:
    print(f"{search_element} does not exit in the tuple")    