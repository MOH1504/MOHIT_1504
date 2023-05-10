#Write a Python program to find the second smallest number in a list. 

def mohit(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[2]

my_list = [1,2,3,4,5,6,7,8,9]
result = mohit(my_list)
print(result)