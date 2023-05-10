#How will you remove last object from a list? Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?
l = [2,33,222,14,25]
print(l)
#l.remove(25)
#print(l)

"""list = [2,33,222,14,25]
here negative indexing starts from right end means the index of 25 is -1
index of 14 corresponds to -2
index of 222 corresports to -3
index of 33 corresports to -4
and index of 2 corresports to -5
so answer to your question is 25
"""

#l.pop
#print(l)

print(l)
print(l[:-5])