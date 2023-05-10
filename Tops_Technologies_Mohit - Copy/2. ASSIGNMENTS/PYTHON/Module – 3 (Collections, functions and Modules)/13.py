#Write a Python program to select an item randomly from a list. 

import random

def item(list):
    return random.choice(list)

my_list = [1,3,4,5,6,4,3,8]
random_item = item(my_list)
print(random_item)