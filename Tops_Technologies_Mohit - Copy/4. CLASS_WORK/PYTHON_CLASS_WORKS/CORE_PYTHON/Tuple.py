"""
Tuple : which is contain similar and dis-similar data elements at single location tuple which is represent by ().

tuple is immutable (we can't change it value)

"""

"""
t = ()
print(t)
print(type(t))

t = ("python",) 
print(t)
print(type(t))

"""

t = ("Python","Java","Android")

l1 = list(t)

l1.remove("Java")

t = tuple(l1)

print(t)