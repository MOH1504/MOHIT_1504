#Write a Python program to convert a list of tuples into a dictionary. 
list = [(1,'a'),(2,'b'),(3,'c'),(4,'d')]

tuple_dict = {key : value for key, value  in list}

print(tuple_dict)