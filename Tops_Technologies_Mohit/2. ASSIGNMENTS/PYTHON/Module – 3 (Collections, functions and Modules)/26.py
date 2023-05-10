#Write a Python program to replace last value of tuples in a list. 

list1 = [("mohit","rakesh","manish"), ("ankit","pooja","raveena"), ("anvi","bhavesh","urmila")]
print(list1)
print([t[:-1]+("gehlot",)for t in list1])