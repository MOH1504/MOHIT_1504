"""
Write a Python program to combine two dictionary adding values for
common keys.
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,'d':400}
Sample output: Counter ({'a': 400, 'b': 400,'d': 400, 'c': 300}). 
"""

d1 = {'a': 100, 'b': 200, 'c':300}

d2 = {'a': 300, 'b': 200,'d':400}

result = {}

for key in d1:
    result[key] =d1[key]
    
for key in d2:
    result[key] = result.get(key, 0) + d2[key]
    
print(result)     