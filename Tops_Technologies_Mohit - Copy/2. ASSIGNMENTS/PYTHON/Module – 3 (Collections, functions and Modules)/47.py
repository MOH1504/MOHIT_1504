# Write a Python program to create a dictionary from a string?
def create_dict_from_string(string):
    words = string.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

string =  "this is a sample string to createa dictionry from a string" 
print(create_dict_from_string(string))      