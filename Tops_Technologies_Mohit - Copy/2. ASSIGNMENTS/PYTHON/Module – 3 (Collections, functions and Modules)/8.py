#Write a Python program to check a list is empty or not.
def is_empty(input_list):
    if len(input_list) == 0:
        return True
    else:
        return False
    
input_list = []
print(is_empty(input_list))

input_list = [1,2,3]
print(is_empty(input_list))
    