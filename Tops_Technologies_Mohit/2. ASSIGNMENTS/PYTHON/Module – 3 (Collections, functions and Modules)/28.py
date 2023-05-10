#Write a Python program to remove an empty tuple(s) from a list of tuples. 
tuples_list = [(1,2,3,4),(),(4,5,6,7),(9,8,7,6)]

filtered_tuple_list = [tup for tup in tuples_list if len(tup) > 0 ]

print(filtered_tuple_list)