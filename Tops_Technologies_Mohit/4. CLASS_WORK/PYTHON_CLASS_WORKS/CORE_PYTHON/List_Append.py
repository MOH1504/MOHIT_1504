# 1) append() : add single element.

# append() :

# accept 5 numbers from user and store it in list :

l1 = []

for i in range(1,6):
    num = int(input("Enter the  number : "))
    l1.append(num)
    print(l1)

# accept 5 numbers from user and store even numbers in evenlist and odd numbers in oddlist (hint : two list)

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


