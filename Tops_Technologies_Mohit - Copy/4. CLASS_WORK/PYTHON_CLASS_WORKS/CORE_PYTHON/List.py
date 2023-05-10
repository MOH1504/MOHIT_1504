# list : blank

#shopping_list = []

#print(shopping_list)

"""
shopping_list = ["fruits","veges","milky products"]

print(shopping_list)

for item in shopping_list:
    print(item)


print(len(shopping_list))


count = 0
shopping_list = ["fruits","veges","milky product"]


for item in shopping_list:
    count+= 1
    print(count)
"""

"""
store data in list :

there are 3 methods

1) append() : add single element
2) extend() : add multiple element in the form of list
3) insert() : add element at specific position
"""

# append() :

# accept 5 numbers from user and store it in list :
"""
l1 = []

for i in range(1,6):
    num = int(input("Enter the  number : "))
    l1.append(num)
    print(l1)
    
"""

# accept 5 numbers from user and store even numbers in evenlist and odd numbers in oddlist (hint : two list)
"""
e_list = []
o_list = []

for i in range(1,6):
    num = int(input("Enter the number : "))
    if num%2 == 0:
        e_list.append(num)
    else:
        o_list.append(num)

print("even list : ",e_list)
print("odd list : ",o_list)

"""
# extends() :

l1 = []
l1.extend([1,2,3,4,56])

print(l1)

"""
l1 = ["C","C++","Java","Android"]

subject = input("Enter your subjects : ")

if subject in l1:
    print("Yes, subject is available")
else:
    print("No, subject is not available")
"""
"""
l1 = [12,23,64,23,8,2,5,3,7]

print(max(l1))
print(min(l1))
print(sum(l1))

"""
"""
l1 = [12,23,64,23,8,2,5,3,7]

l1.sort()
print(l1)

l1.sort(reverse = True)
print(l1)

"""
"""
l1 = [12,34,87,3,67,23,67,23,12]

data = []

for i in l1:
    if i not in data:
        data.append(i)
print(l1)
print(data)

"""
"""
# List slicing :

# starting index - 0

l1 = [12,34,67,8,34,6,2,8]

print(l1[:3]) # first 3 values

print(l1[2:5]) # between values

print(l1[-1]) # last value

print(l1[-4:-1])

print(l1[-4:])

"""

# insert() :
"""
l1 = [12,23,45,67,45,78]

l1.insert(0,10001)
print(l1)
"""

"""
# pop : it will remove last element from the list.

l1.pop()
print(l1)

"""

"""
# remove element from specific index position.

l1.pop(2)
print(l1)

"""

l1 = [12,23,45,67,45,78]
# value wise remove :
l1.remove(45)

print(l1)

print(l1.index(78))

# clear:
l1.clear()

print(l1)

# delete:
del l1
print(l1)