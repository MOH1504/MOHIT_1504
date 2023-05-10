#Write a Python program to unzip a list of tuples into individual lists. 
tuples_list = [(1,'a'),(2,'b'),(3,'c'),(4,'d')]

lists = zip(*tuples_list)
lists = [list(lst) for lst in lists]

print(lists)