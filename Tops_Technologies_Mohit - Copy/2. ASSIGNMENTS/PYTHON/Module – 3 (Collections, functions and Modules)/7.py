#Write a Python program to remove duplicates from a list.
def remove_duplicates(input_list):
    return list(set(input_list))

input_list = [1, 2, 3, 1, 2, 4, 5, 6, 4, 7, 8, 9]
print(remove_duplicates(input_list))