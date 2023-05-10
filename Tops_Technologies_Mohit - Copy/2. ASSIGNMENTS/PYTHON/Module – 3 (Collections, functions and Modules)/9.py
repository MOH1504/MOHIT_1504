#Write a Python function that takes two lists and returns true if they have at least one common member. 

def common_member(list1,list2):
    return len(set(list1).intersection(list2)) > 0

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
print(common_member(list1,list2))

list1 = [1,2,3,4,5]
list2 = [4,5,6,1,7]
print(common_member(list1,list2))