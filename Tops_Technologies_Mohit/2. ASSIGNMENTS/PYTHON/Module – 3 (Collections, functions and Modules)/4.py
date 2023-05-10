#Write a Python function to get the largest number, smallest num and sum of all from a list.

lst = []
num = int (input("how many numbers : "))
for n in range(num):
    number = int(input("enter numbers "))
    lst.append(number)
print("maximum element in the list is :",max (lst),"\nminimum element in the list is :",min(lst))
     