# Write a Python script to check if a given key already exists in a dictionary?
dict1 = {'name' : 'mohit', 'age' : 22, 'gander' : 'male'}

key = 'age'

if key in dict1:
    print(f"key '{key}' existed in the dictionry.")
else:
    print(f"key'{key}' dose not exit in the dictionry.")    