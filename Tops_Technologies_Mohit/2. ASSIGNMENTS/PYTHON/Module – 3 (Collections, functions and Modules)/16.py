#Write a Python program to check whether a list contains a sub list?
def sublist(lst,sublst):
    n = len(sublst)
    return any([sublst == lst[i:i+n] for i in range (len(lst) - n + 1)])

list1 = [1,1,2,3,4,5,6]
list2 = [1,2,3,4,5,6]
list3 = [2,3,4,5]

print(sublist(list1,list2))
print(sublist(list1,list3))